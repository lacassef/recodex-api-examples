# Feed naming patterns

Use `GET /api/livescores/feed/{version}/{feed}` when you already have a feed name. The patterns below are the usual names. A sport or a match can return `204` when that feed has no data.

When a named route exists, call it. The named routes are in the area pages linked from the [map](../README.md).

## Scoreboards and refresh

- Scoreboard: `f_{sportId}_{dayOffset}_2_{lang}_1`
  - Example: `f_1_0_2_en_1`
- Refresh: `r_{sportId}_1`
  - Example: `r_1_1`

## Odds list

- Odds list: `fo_{sportId}_{dayOffset}_2_{lang}_1_0`
  - Example: `fo_1_0_2_en_1_0`

## Match detail feeds

Use `{eventId}` from `sharedindexes_event_id` in a match list.

- Match stats: `df_st_1_{eventId}`
- Box score: `df_psp_1_{eventId}`
- Box score names: `df_psn_1_{eventId}`
- Live table: `df_tl_1_{eventId}`
- Live commentary: `df_lc_1_{eventId}`
- Commentary only: `df_lcpo_1_{eventId}`
- Point by point: `df_mh_1_{eventId}`
- Head to head: `df_hh_1_{eventId}`
- Match news: `df_nf_1_{eventId}`
- Match report: `df_mr_1_{eventId}`
- Current tennis game: `df_mhs_1_{eventId}`
- Highlight videos: `df_hi_1_{eventId}`
- Vertical summary: `df_sui_1_{eventId}`
- Horizontal summary: `df_sur_1_{eventId}`
- Odds detail: `df_dos_1_{eventId}_`

## Tournament feeds

- Tables: `tx_{tournamentId}_{stageId}`
  - Example: `tx_M1c7lv64_tKE3WZmL`
- Match lists:
  - `p_1_165_OC8T8zk3_2_en_1`
  - `t_2_5733_MTJqK2xP_2_en_1`
  - `pr_2_182_GrsQDFC0_1_2_en_1_s`

## Rankings feeds

- Rankings: `ran_{rankingId}_1` or `ral_{rankingId}_1`
  - Example: `ran_dSJr14Y8_1`

## Other prefixes

- Category tournaments: `c_*`
- Match hash detail: `g_*`
- Featured lists: `fp_*`
- System status: `sys_*`
