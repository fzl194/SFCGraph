---
id: UNC@20.15.2@MMLCommand@RMV NRFBSFINDEXRT
type: MMLCommand
name: RMV NRFBSFINDEXRT（删除BSFINDEX路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFBSFINDEXRT
command_category: 配置类
applicable_nf:
- NRF
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- NRF业务及策略管理
- 分层NRF管理
- NRF路由配置
- BSF路由管理
status: active
---

# RMV NRFBSFINDEXRT（删除BSFINDEX路由）

## 功能

**适用NF：NRF**

该命令用删除选择BSF时的路由实例信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BSFINDEX | BSF索引 | 可选必选说明：必选参数<br>参数含义：该参数用于表示BSF路由实例信息的索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~65535。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于BSF类型寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFBSFINDEXRT]] · BSFINDEX路由（NRFBSFINDEXRT）

## 使用实例

删除H-NRF1上BSF索引为1时对应的下一跳路由：

```
RMV NRFBSFINDEXRT: BSFINDEX=1, NEXTNRFGRPNAME="L-NRF";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFBSFINDEXRT.md`
