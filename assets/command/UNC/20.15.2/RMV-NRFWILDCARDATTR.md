---
id: UNC@20.15.2@MMLCommand@RMV NRFWILDCARDATTR
type: MMLCommand
name: RMV NRFWILDCARDATTR（删除分层互联通配属性）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: NRFWILDCARDATTR
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

# RMV NRFWILDCARDATTR（删除分层互联通配属性）

## 功能

**适用NF：NRF**

该命令用于在NRF删除分层互联通配属性，以减少分层互联路由信息的配置量。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRIBUTE | 属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分层互联属性类型。<br>数据来源：全网规划<br>取值范围：<br>- TAC（TAC）<br>- NRFNFGROUP（NFGROUP）<br>- SERVINGSCOPE（SERVINGSCOPE）<br>- REGIONIDSETID（区域标识和集合标识）<br>- ROUTINGINDICATOR（选路指示器）<br>默认值：无<br>配置原则：<br>每种属性最多只能配置一条分层互联通配属性。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFWILDCARDATTR]] · 分层互联通配属性（NRFWILDCARDATTR）

## 使用实例

运营商完成分层互联路由配置后，不需要通配属性，想删除属性为NRFNFGROUP的分层互联通配属性信息时，执行此命令。

```
RMV NRFWILDCARDATTR: ATTRIBUTE=NRFNFGROUP;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/RMV-NRFWILDCARDATTR.md`
