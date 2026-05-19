

import sys
import io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# =============================================================================
# STEP 1: DATA INGESTION & CLEANING
# =============================================================================
print("=" * 70)
print("STEP 1: DATA INGESTION & CLEANING")
print("=" * 70)

df = pd.read_csv('Hotel_bookings_final.csv')
print(f"Dataset loaded: {df.shape[0]:,} rows x {df.shape[1]} columns\n")

date_cols = ['booking_date', 'check_in_date', 'check_out_date', 'travel_date']
for col in date_cols:
    df[col] = pd.to_datetime(df[col], errors='coerce')

df['lead_time'] = (df['check_in_date'] - df['booking_date']).dt.days
df['stay_length'] = (df['check_out_date'] - df['check_in_date']).dt.days
df['booking_month'] = df['booking_date'].dt.to_period('M').astype(str)
df['booking_month_num'] = df['booking_date'].dt.month
df['profit_margin'] = df['markup'] / df['costprice'] * 100
df['is_cancelled'] = (df['booking_status'] == 'Cancelled').astype(int)

null_checkin = df['check_in_date'].isna()
print(f"Rows with missing check-in date : {null_checkin.sum():,}")
print(f"  -> Of those, cancelled         : {(df.loc[null_checkin, 'booking_status'] == 'Cancelled').sum():,}")
print(f"  -> Of those, failed            : {(df.loc[null_checkin, 'booking_status'] == 'Failed').sum():,}")

# =============================================================================
# STEP 2: KEY METRICS CALCULATION
# =============================================================================
print("\n" + "=" * 70)
print("STEP 2: KEY METRICS")
print("=" * 70)

total_bookings = len(df)
confirmed = (df['booking_status'] == 'Confirmed').sum()
cancelled = (df['booking_status'] == 'Cancelled').sum()
failed = (df['booking_status'] == 'Failed').sum()

cancel_rate = cancelled / total_bookings * 100
fail_rate = failed / total_bookings * 100
success_rate = confirmed / total_bookings * 100

avg_lead_time = df['lead_time'].mean()
avg_stay = df['stay_length'].mean()
avg_booking_val = df['booking_value'].mean()
total_revenue = df.loc[df['booking_status'] == 'Confirmed', 'selling_price'].sum()

print(f"Total Bookings       : {total_bookings:,}")
print(f"Confirmed            : {confirmed:,} ({success_rate:.1f}%)")
print(f"Cancelled            : {cancelled:,} ({cancel_rate:.1f}%)")
print(f"Failed               : {failed:,} ({fail_rate:.1f}%)")
print(f"Avg Lead Time        : {avg_lead_time:.1f} days")
print(f"Avg Stay Length      : {avg_stay:.1f} days")
print(f"Avg Booking Value    : ${avg_booking_val:,.0f}")
print(f"Total Confirmed Rev  : ${total_revenue:,.0f}")

# =============================================================================
# STEP 3: DETAILED CROSS-TABULATIONS
# =============================================================================
print("\n" + "=" * 70)
print("STEP 3: CROSS-TAB ANALYSIS")
print("=" * 70)

chan_agg = df.groupby('booking_channel').agg(
    bookings=('booking_status', 'count'),
    cancel_count=('is_cancelled', 'sum'),
    avg_value=('booking_value', 'mean'),
    avg_markup=('markup', 'mean'),
    avg_lead=('lead_time', 'mean'),
    avg_stay=('stay_length', 'mean'),
).reset_index()
chan_agg['cancel_rate'] = (chan_agg['cancel_count'] / chan_agg['bookings'] * 100).round(2)
print("\n-- Booking Channel Summary --")
print(chan_agg.to_string(index=False))

room_agg = df.groupby('room_type').agg(
    bookings=('booking_status', 'count'),
    cancel_count=('is_cancelled', 'sum'),
    avg_value=('booking_value', 'mean'),
    avg_markup=('markup', 'mean'),
).reset_index()
room_agg['cancel_rate'] = (room_agg['cancel_count'] / room_agg['bookings'] * 100).round(2)
print("\n-- Room Type Summary --")
print(room_agg.to_string(index=False))

star_agg = df.groupby('star_rating').agg(
    bookings=('booking_status', 'count'),
    cancel_count=('is_cancelled', 'sum'),
    avg_value=('booking_value', 'mean'),
    avg_selling=('selling_price', 'mean'),
).reset_index()
star_agg['cancel_rate'] = (star_agg['cancel_count'] / star_agg['bookings'] * 100).round(2)
print("\n-- Star Rating Summary --")
print(star_agg.to_string(index=False))

monthly = df.groupby('booking_month').agg(
    total_bookings=('booking_status', 'count'),
    cancellations=('is_cancelled', 'sum'),
    avg_value=('booking_value', 'mean'),
    total_value=('booking_value', 'sum'),
).reset_index()
monthly['cancel_rate'] = (monthly['cancellations'] / monthly['total_bookings'] * 100).round(2)
print("\n-- Monthly Trends --")
print(monthly.to_string(index=False))

# =============================================================================
# STEP 4: VISUALIZATIONS (Individual Charts)
# =============================================================================
print("\n" + "=" * 70)
print("STEP 4: GENERATING VISUALIZATIONS")
print("=" * 70)

months_str = monthly['booking_month'].values
cancel_rates = monthly['cancel_rate'].values

# --- 1. Booking Status Pie ---
fig, ax = plt.subplots(figsize=(7, 7))
status_counts = df['booking_status'].value_counts()
ax.pie(status_counts.values, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
ax.set_title('Booking Status Distribution', fontsize=14, fontweight='bold', pad=12)
plt.savefig('chart01_booking_status_pie.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart01_booking_status_pie.png")

# --- 2. Cancellation Rate by Channel ---
fig, ax = plt.subplots(figsize=(8, 4))
chan_cancel = df.groupby('booking_channel')['is_cancelled'].mean().sort_values() * 100
bars = ax.barh(chan_cancel.index, chan_cancel.values, height=0.5)
for bar, val in zip(bars, chan_cancel.values):
    ax.text(bar.get_width() + 0.5, bar.get_y() + bar.get_height() / 2,
            f'{val:.1f}%', va='center', fontweight='bold', fontsize=10)
ax.set_xlabel('Cancellation Rate (%)')
ax.set_title('Cancellation Rate by Booking Channel', fontsize=14, fontweight='bold', pad=12)
ax.set_xlim(0, 35)
plt.savefig('chart02_cancel_rate_by_channel.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart02_cancel_rate_by_channel.png")

# --- 3. Avg Booking Value by Channel ---
fig, ax = plt.subplots(figsize=(8, 4))
chan_val = df.groupby('booking_channel')['booking_value'].mean().sort_values()
bars = ax.barh(chan_val.index, chan_val.values, height=0.5)
for bar, val in zip(bars, chan_val.values):
    ax.text(bar.get_width() + 200, bar.get_y() + bar.get_height() / 2,
            f'${val:,.0f}', va='center', fontweight='bold', fontsize=10)
ax.set_xlabel('Avg Booking Value ($)')
ax.set_title('Avg Booking Value by Channel', fontsize=14, fontweight='bold', pad=12)
ax.set_xlim(0, 35000)
plt.savefig('chart03_avg_value_by_channel.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart03_avg_value_by_channel.png")

# --- 4. Monthly Cancellation Rate Trend ---
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(len(months_str)), cancel_rates, linewidth=2.5, marker='o', markersize=6)
for i, val in enumerate(cancel_rates):
    ax.annotate(f'{val:.1f}%', (i, val), textcoords='offset points',
                xytext=(0, 10), ha='center', fontsize=8, fontweight='bold')
ax.set_xticks(range(len(months_str)))
ax.set_xticklabels(months_str, rotation=45, ha='right')
ax.set_ylabel('Cancellation Rate (%)')
ax.set_title('Monthly Cancellation Rate Trend', fontsize=14, fontweight='bold', pad=12)
ax.axhline(cancel_rate, color='gray', ls='--', lw=1, alpha=0.6)
plt.savefig('chart04_monthly_cancel_trend.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart04_monthly_cancel_trend.png")

# --- 5. Cancellation Rate by Star Rating ---
fig, ax = plt.subplots(figsize=(7, 4))
star_cancel = df.groupby('star_rating')['is_cancelled'].mean() * 100
bars = ax.bar(star_cancel.index.astype(str), star_cancel.values, width=0.6)
for bar, val in zip(bars, star_cancel.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f'{val:.1f}%', ha='center', fontweight='bold', fontsize=9)
ax.set_xlabel('Star Rating')
ax.set_ylabel('Cancellation Rate (%)')
ax.set_title('Cancellation Rate by Star Rating', fontsize=14, fontweight='bold', pad=12)
ax.set_ylim(0, 28)
plt.savefig('chart05_cancel_by_star.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart05_cancel_by_star.png")

# --- 6. Booking Volume by Channel & Status (Stacked) ---
fig, ax = plt.subplots(figsize=(8, 5))
status_by_chan = pd.crosstab(df['booking_channel'], df['booking_status'])
status_by_chan = status_by_chan[['Confirmed', 'Cancelled', 'Failed']]
status_by_chan.plot(kind='bar', stacked=True, ax=ax, width=0.65)
ax.set_title('Booking Volume by Channel & Status', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Number of Bookings')
ax.set_xlabel('')
ax.tick_params(axis='x', rotation=0)
plt.savefig('chart06_volume_by_channel_status.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart06_volume_by_channel_status.png")

# --- 7. Booking Value Distribution by Channel (Box Plot) ---
fig, ax = plt.subplots(figsize=(8, 5))
channel_order = ['Web', 'Mobile App', 'Travel Agent']
sns.boxplot(data=df, x='booking_channel', y='booking_value', order=channel_order,
            ax=ax, flierprops={'marker': '.', 'markersize': 2, 'alpha': 0.3}, width=0.5)
ax.set_title('Booking Value Distribution by Channel', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Booking Value ($)')
ax.set_xlabel('')
plt.savefig('chart07_value_boxplot_channel.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart07_value_boxplot_channel.png")

# --- 8. Platform vs Booking Channel ---
fig, ax = plt.subplots(figsize=(8, 5))
platform_chan = pd.crosstab(df['channel_of_booking'], df['booking_channel'])
platform_chan.plot(kind='bar', ax=ax, width=0.7)
ax.set_title('Platform vs Booking Channel', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Number of Bookings')
ax.set_xlabel('')
ax.tick_params(axis='x', rotation=0)
plt.savefig('chart08_platform_vs_channel.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart08_platform_vs_channel.png")

# --- 9. Cancellation Rate by Room Type ---
fig, ax = plt.subplots(figsize=(7, 4))
room_cancel = df.groupby('room_type')['is_cancelled'].mean() * 100
bars = ax.bar(room_cancel.index, room_cancel.values, width=0.5)
for bar, val in zip(bars, room_cancel.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f'{val:.1f}%', ha='center', fontweight='bold', fontsize=11)
ax.set_title('Cancellation Rate by Room Type', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Cancellation Rate (%)')
ax.set_ylim(0, 30)
plt.savefig('chart09_cancel_by_room.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart09_cancel_by_room.png")

# --- 10. Booking Volume by Room & Status ---
fig, ax = plt.subplots(figsize=(8, 5))
status_by_room = pd.crosstab(df['room_type'], df['booking_status'])
status_by_room = status_by_room[['Confirmed', 'Cancelled', 'Failed']]
status_by_room.plot(kind='bar', ax=ax, width=0.65)
ax.set_title('Booking Volume by Room Type & Status', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Count')
ax.set_xlabel('')
ax.tick_params(axis='x', rotation=0)
plt.savefig('chart10_volume_by_room_status.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart10_volume_by_room_status.png")

# --- 11. Avg Booking Value by Star Rating & Status ---
fig, ax = plt.subplots(figsize=(8, 5))
star_val = df.groupby(['star_rating', 'booking_status'])['booking_value'].mean().unstack()
star_val = star_val[['Confirmed', 'Cancelled', 'Failed']]
star_val.plot(kind='bar', ax=ax, width=0.7)
ax.set_title('Avg Booking Value: Star Rating x Status', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Avg Booking Value ($)')
ax.set_xlabel('Star Rating')
ax.tick_params(axis='x', rotation=0)
plt.savefig('chart11_value_star_status.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart11_value_star_status.png")

# --- 12. Profit Margin by Room Type (Violin) ---
fig, ax = plt.subplots(figsize=(8, 5))
room_margin = df.dropna(subset=['profit_margin'])
sns.violinplot(data=room_margin, x='room_type', y='profit_margin', ax=ax, inner='quartile')
ax.set_title('Profit Margin Distribution by Room Type', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Profit Margin (%)')
ax.set_xlabel('')
plt.savefig('chart12_margin_violin.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart12_margin_violin.png")

# --- 13. Monthly Total Booking Value ---
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(len(monthly)), monthly['total_value'] / 1e6, linewidth=2.5, marker='o', markersize=5)
ax.set_xticks(range(len(monthly)))
ax.set_xticklabels(monthly['booking_month'], rotation=45, ha='right')
ax.set_ylabel('Total Booking Value ($M)')
ax.set_title('Monthly Total Booking Value', fontsize=14, fontweight='bold', pad=10)
plt.savefig('chart13_monthly_total_value.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart13_monthly_total_value.png")

# --- 14. Monthly Average Booking Value ---
fig, ax = plt.subplots(figsize=(12, 5))
ax.plot(range(len(monthly)), monthly['avg_value'] / 1e3, linewidth=2.5, marker='s', markersize=5)
ax.set_xticks(range(len(monthly)))
ax.set_xticklabels(monthly['booking_month'], rotation=45, ha='right')
ax.set_ylabel('Avg Booking Value ($K)')
ax.set_title('Monthly Average Booking Value', fontsize=14, fontweight='bold', pad=10)
plt.savefig('chart14_monthly_avg_value.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart14_monthly_avg_value.png")

# --- 15. Stay Length Distribution by Purpose ---
fig, ax = plt.subplots(figsize=(8, 5))
sns.histplot(data=df.dropna(subset=['stay_length']), x='stay_length', hue='stay_type',
             ax=ax, multiple='dodge', bins=7, alpha=0.8)
ax.set_title('Stay Length Distribution by Purpose', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Stay Length (days)')
ax.set_ylabel('Count')
plt.savefig('chart15_stay_length_dist.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart15_stay_length_dist.png")

# --- 16. Lead Time: Confirmed vs Cancelled ---
fig, ax = plt.subplots(figsize=(8, 5))
lead_data = df.dropna(subset=['lead_time'])
for status in ['Confirmed', 'Cancelled']:
    subset = lead_data[lead_data['booking_status'] == status]['lead_time']
    ax.hist(subset, bins=30, alpha=0.5, label=status)
ax.set_title('Lead Time: Confirmed vs Cancelled', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Lead Time (days)')
ax.set_ylabel('Count')
ax.legend()
plt.savefig('chart16_lead_time_comparison.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart16_lead_time_comparison.png")

# --- 17. Missing Check-in & Cancellation ---
fig, ax = plt.subplots(figsize=(8, 5))
missing_data = pd.DataFrame({
    'Category': ['Has Check-in Date', 'Missing Check-in Date'],
    'Cancelled': [
        df[~null_checkin]['is_cancelled'].mean() * 100,
        df[null_checkin]['is_cancelled'].mean() * 100
    ],
    'Not Cancelled': [
        (1 - df[~null_checkin]['is_cancelled'].mean()) * 100,
        (1 - df[null_checkin]['is_cancelled'].mean()) * 100
    ]
})
ax.bar(missing_data['Category'], missing_data['Cancelled'], label='Cancelled', width=0.5)
ax.bar(missing_data['Category'], missing_data['Not Cancelled'],
       bottom=missing_data['Cancelled'], label='Not Cancelled', width=0.5)
for i, val in enumerate(missing_data['Cancelled']):
    ax.text(i, val / 2, f'{val:.1f}%', ha='center', va='center', fontweight='bold', fontsize=11)
ax.set_title('Missing Check-in & Cancellation', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Percentage')
ax.legend(loc='upper right')
plt.savefig('chart17_missing_checkin.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart17_missing_checkin.png")

# --- 18. Booking Status by Refund Eligibility ---
fig, ax = plt.subplots(figsize=(8, 5))
refund_cancel = pd.crosstab(df['refund_status'], df['booking_status'], normalize='index') * 100
refund_cancel = refund_cancel[['Confirmed', 'Cancelled', 'Failed']]
refund_cancel.plot(kind='bar', stacked=True, ax=ax, width=0.5)
ax.set_title('Booking Status by Refund Eligibility', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Percentage (%)')
ax.set_xlabel('Refund Status')
ax.tick_params(axis='x', rotation=0)
plt.savefig('chart18_refund_status.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart18_refund_status.png")

# --- 19. Cancellation Rate by City ---
fig, ax = plt.subplots(figsize=(8, 6))
city_cancel = df.groupby('city')['is_cancelled'].mean().sort_values(ascending=True) * 100
ax.barh(city_cancel.index, city_cancel.values, height=0.6)
for i, (idx, val) in enumerate(city_cancel.items()):
    ax.text(val + 0.3, i, f'{val:.1f}%', va='center', fontsize=9)
ax.axvline(cancel_rate, color='gray', ls='--', lw=1, alpha=0.6)
ax.set_title('Cancellation Rate by City', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Cancellation Rate (%)')
plt.savefig('chart19_cancel_by_city.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart19_cancel_by_city.png")

# --- 20. Cancellation Rate by Payment Method ---
fig, ax = plt.subplots(figsize=(7, 4))
pay_cancel = df.groupby('payment_method')['is_cancelled'].mean().sort_values() * 100
bars = ax.bar(pay_cancel.index, pay_cancel.values, width=0.5)
for bar, val in zip(bars, pay_cancel.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f'{val:.1f}%', ha='center', fontweight='bold', fontsize=10)
ax.set_title('Cancellation Rate by Payment Method', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Cancellation Rate (%)')
ax.set_ylim(0, 28)
plt.savefig('chart20_cancel_by_payment.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart20_cancel_by_payment.png")

# --- 21. Heatmap: Avg Booking Value (Channel x Room) ---
fig, ax = plt.subplots(figsize=(8, 5))
heatmap_val = df.pivot_table(values='booking_value', index='booking_channel',
                              columns='room_type', aggfunc='mean')
sns.heatmap(heatmap_val, annot=True, fmt=',.0f', cmap='YlOrRd', ax=ax,
            linewidths=2, annot_kws={'fontsize': 11, 'fontweight': 'bold'})
ax.set_title('Avg Booking Value ($): Channel x Room Type', fontsize=14, fontweight='bold', pad=10)
plt.savefig('chart21_heatmap_value.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart21_heatmap_value.png")

# --- 22. Heatmap: Cancellation Rate (Channel x Star Rating) ---
fig, ax = plt.subplots(figsize=(8, 5))
heatmap_cancel = df.pivot_table(values='is_cancelled', index='booking_channel',
                                  columns='star_rating', aggfunc='mean') * 100
sns.heatmap(heatmap_cancel, annot=True, fmt='.1f', cmap='RdYlGn_r', ax=ax,
            linewidths=2, annot_kws={'fontsize': 11, 'fontweight': 'bold'})
ax.set_title('Cancellation Rate (%): Channel x Star Rating', fontsize=14, fontweight='bold', pad=10)
plt.savefig('chart22_heatmap_cancel.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart22_heatmap_cancel.png")

# --- 23. Coupon Usage vs Cancellation ---
fig, ax = plt.subplots(figsize=(7, 4))
coupon_cancel = df.groupby('Coupon USed?')['is_cancelled'].mean() * 100
bars = ax.bar(coupon_cancel.index, coupon_cancel.values, width=0.45)
for bar, val in zip(bars, coupon_cancel.values):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.3,
            f'{val:.1f}%', ha='center', fontweight='bold', fontsize=12)
ax.set_title('Cancellation Rate: Coupon Users', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Cancellation Rate (%)')
ax.set_xlabel('Coupon Used?')
ax.set_ylim(0, 28)
plt.savefig('chart23_coupon_cancel.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart23_coupon_cancel.png")

# --- 24. Cashback Distribution by Status ---
fig, ax = plt.subplots(figsize=(8, 5))
for status in ['Confirmed', 'Cancelled']:
    subset = df[df['booking_status'] == status]['cashback']
    ax.hist(subset, bins=30, alpha=0.5, label=status)
ax.set_title('Cashback Distribution by Status', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Cashback Amount')
ax.set_ylabel('Count')
ax.legend()
plt.savefig('chart24_cashback_dist.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart24_cashback_dist.png")

# --- 25. Booking Status by Rooms Booked ---
fig, ax = plt.subplots(figsize=(8, 5))
rooms_status = pd.crosstab(df['num_rooms_booked'], df['booking_status'])
rooms_status = rooms_status[['Confirmed', 'Cancelled', 'Failed']]
rooms_status.plot(kind='bar', ax=ax, width=0.7)
ax.set_title('Booking Status by Number of Rooms Booked', fontsize=14, fontweight='bold', pad=10)
ax.set_ylabel('Count')
ax.set_xlabel('Number of Rooms')
ax.tick_params(axis='x', rotation=0)
plt.savefig('chart25_rooms_booked_status.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart25_rooms_booked_status.png")

# --- 26. Avg Booking Value by City ---
fig, ax = plt.subplots(figsize=(9, 6))
city_val = df.groupby('city')['booking_value'].mean().sort_values()
ax.barh(city_val.index, city_val.values, height=0.6)
for i, (idx, val) in enumerate(city_val.items()):
    ax.text(val + 100, i, f'${val:,.0f}', va='center', fontsize=9)
ax.set_title('Avg Booking Value by City', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Avg Booking Value ($)')
plt.savefig('chart26_avg_value_by_city.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart26_avg_value_by_city.png")

# --- 27. Total Confirmed Revenue by City ---
fig, ax = plt.subplots(figsize=(9, 6))
city_rev = df[df['booking_status'] == 'Confirmed'].groupby('city')['selling_price'].sum().sort_values()
ax.barh(city_rev.index, city_rev.values / 1e6, height=0.6)
for i, (idx, val) in enumerate((city_rev / 1e6).items()):
    ax.text(val + 0.2, i, f'${val:.1f}M', va='center', fontsize=9)
ax.set_title('Total Confirmed Revenue by City', fontsize=14, fontweight='bold', pad=10)
ax.set_xlabel('Revenue ($M)')
plt.savefig('chart27_revenue_by_city.png', bbox_inches='tight', pad_inches=0.3)
plt.close()
print("[OK] chart27_revenue_by_city.png")

# =============================================================================
# STEP 5: SUMMARY
# =============================================================================
print("\n" + "=" * 70)
print("STEP 5: SUMMARY REPORT DATA")
print("=" * 70)

print(f"""
Total Bookings           : {total_bookings:>10,}
Confirmed Bookings       : {confirmed:>10,}  ({success_rate:.1f}%)
Cancelled Bookings       : {cancelled:>10,}  ({cancel_rate:.1f}%)
Failed Bookings          : {failed:>10,}  ({fail_rate:.1f}%)
Average Lead Time        : {avg_lead_time:>10.1f} days
Average Stay Length      : {avg_stay:>10.1f} days
Average Booking Value    : ${avg_booking_val:>10,.0f}
Total Confirmed Revenue  : ${total_revenue:>12,.0f}
""")

print("\n[DONE] Analysis complete! All 27 chart files saved to current directory.")
print("   Files: chart01 through chart27")
