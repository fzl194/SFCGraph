---
id: UNC@20.15.2@MMLCommand@RMV NRFWILDCARDSTRRT
type: MMLCommand
name: RMV NRFWILDCARDSTRRT（删除分层互联信元字符串通配属性路由）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFWILDCARDSTRRT
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
- NRF路由通配属性配置
status: active
---

# RMV NRFWILDCARDSTRRT（删除分层互联信元字符串通配属性路由）

## 功能

**适用NF：NRF**

该命令用于删除目标分层互联信元字符串通配属性的路由信息。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRIBUTE | 属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分层互联属性类型。<br>数据来源：全网规划<br>取值范围：<br>- TAC（TAC）<br>- NRFNFGROUP（NFGROUP）<br>- SERVINGSCOPE（SERVINGSCOPE）<br>- REGIONIDSETID（区域标识和集合标识）<br>- ROUTINGINDICATOR（选路指示器）<br>默认值：无<br>配置原则：无 |
| MATCHSTR | 通配字符串 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分层互联信元字符串通配值。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~128。<br>默认值：无<br>配置原则：<br>通配字符串的长度应该与ADD NRFWILDCARDATTR命令中对应属性配置的通配长度相同。 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示NRF基于通配字符串寻址NF时的下一跳NRF实例组名称，该参数需要输入时，必须通过LST NRFGROUP命令获取。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFWILDCARDSTRRT]] · 分层互联信元字符串通配属性路由（NRFWILDCARDSTRRT）

## 使用实例

运营商想通过此命令在当前NRF上删除一条支持字符串通配值为"042"（运营商规划）所对应的特定通配属性的下一跳路由为nrfgroup001的路由信息。

```
RMV NRFWILDCARDSTRRT: ATTRIBUTE=TAC, MATCHSTR="042", NEXTNRFGRPNAME="L-NRF";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除分层互联信元字符串通配属性路由（RMV-NRFWILDCARDSTRRT）_96242905.md`
