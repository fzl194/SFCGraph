---
id: UNC@20.15.2@MMLCommand@MOD NRFDNNRT
type: MMLCommand
name: MOD NRFDNNRT（修改DNN路由）
nf: UNC
version: 20.15.2
verb: MOD
object_keyword: NRFDNNRT
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
- DNN路由管理
status: active
---

# MOD NRFDNNRT（修改DNN路由）

## 功能

**适用NF：NRF**

该命令用于修改指定DNN路由所归属的NRF实例组名称。

## 注意事项

- 该命令执行后立即生效。

- 根据输入参数条件，如果待修改的记录在系统中只存在一条，则直接执行此命令进行修改。
- 根据输入参数条件，如果待修改的记录在系统中可以匹配到多条，则系统无法判断待修改记录具体是哪一条，不能通过此MOD命令进行修改，此时需要执行对应的RMV记录先删除待修改记录，再执行对应ADD命令新增新的记录（修改后的记录）完成修改。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| DNN | 数据网络名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示数据网络名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~50。该参数不区分大小写。<br>默认值：无<br>配置原则：<br>当前NRF仅支持NFTYPE为PCF的路由转发功能，其他NF类型为预留功能。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：可选参数<br>参数含义：该参数用于表示当前NRF基于DNN寻址NF时的下一跳NRF实例组名称，被寻址的NF归属于该NRF实例组。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFDNNRT]] · DNN路由（NRFDNNRT）

## 使用实例

运营商网络规划变更，当前NRF上寻址DNN下一跳路由发生变化时，需要执行：

```
MOD NRFDNNRT: DNN="huawei.com", NEXTNRFGRPNAME="L-NRF3";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/MOD-NRFDNNRT.md`
