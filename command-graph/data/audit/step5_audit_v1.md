# Step 5 审计报告 v1

## 统计

- 处理命令数: 4577
- 总关系数: 13062

## 关系类型分布

- param_condition: 2723
- cmd_reference: 2116
- effect_timing: 1565
- cmd_prerequisite: 603
- risk_level: 305
- param_exclusion: 101
- config_object_hierarchy: 58

### cmd_prerequisite 样本

- **RMV NGBINDDFSRPAIR** → **ADD NGBINDDFSRPAIR**: 双发选收结对已绑定该5G LAN会话实例
  > 双发选收结对已绑定该5G LAN会话实例。
- **ADD NGBINDDFSRPAIR** → **ADD NGBINDDFSRPAIR**: 双发选收结对存在
  > 双发选收结对存在。
- **ADD NGBINDDFSRPAIR** → **ADD NGBINDDFSRPAIR**: 双发选收结对未绑定其它5G LAN会话实例
  > 双发选收结对未绑定其它5G LAN会话实例。
- **ADD DFSRPAIRMEM** → **ADD DFSRPAIR**: 执行ADD DFSRPAIRMEM前必须先执行ADD DFSRPAIR创建双发选收结对
  > 双发选收结对存在。
- **MOD DFSRPAIR** → **ADD DFSRPAIR**: 修改双发选收结对配置前，该记录必须已经存在。
  > 该记录必须已经存在。

### cmd_reference 样本

- **LST NGVNVLANMAP** → **ADD NGVNVLANMAP**: 输出结果说明中引用了ADD NGVNVLANMAP的参数说明
  > 参见ADD NGVNVLANMAP的参数说明。
- **RMV NGVNVLANWL** → **ADD NGVNINSTANCE**: VNINSTANCE参数使用ADD NGVNINSTANCE命令配置生成
  > 该参数使用ADD NGVNINSTANCE命令配置生成。
- **ADD NGVNVLANWL** → **ADD NGVNINSTANCE**: VNINSTANCE参数使用ADD NGVNINSTANCE命令配置生成
  > 该参数使用ADD NGVNINSTANCE命令配置生成。
- **LST NGVNVLANWL** → **ADD NGVNINSTANCE**: 参数VNINSTANCE使用ADD NGVNINSTANCE命令配置生成
  > 该参数使用ADD NGVNINSTANCE命令配置生成。
- **LST NGVNVLANWL** → **ADD NGVNVLANWL**: 输出结果说明参见ADD NGVNVLANWL的参数说明
  > 参见ADD NGVNVLANWL的参数说明。

### param_condition 样本

- **DIRECTION** → **VTEPNAME**: 可选
  > 该参数在“DIRECTION”配置为“TO_N6”时为可选参数。
- **IPVERSION** → **SRCIPV4ADDR**: 必选
  > 该参数在“IPVERSION”配置为“IPv4”时为必选参数。
- **IPVERSION** → **SRCIPV6ADDR**: 必选
  > 该参数在“IPVERSION”配置为“IPv6”时为必选参数。
- **IPVERSION** → **DSTIPV4ADDR**: 必选
  > 该参数在“IPVERSION”配置为“IPv4”时为必选参数。
- **IPVERSION** → **DSTIPV6ADDR**: 必选
  > 该参数在“IPVERSION”配置为“IPv6”时为必选参数。
