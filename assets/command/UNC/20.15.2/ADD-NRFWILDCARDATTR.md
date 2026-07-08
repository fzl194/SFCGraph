---
id: UNC@20.15.2@MMLCommand@ADD NRFWILDCARDATTR
type: MMLCommand
name: ADD NRFWILDCARDATTR（增加分层互联通配属性）
nf: UNC
version: 20.15.2
verb: ADD
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

# ADD NRFWILDCARDATTR（增加分层互联通配属性）

## 功能

**适用NF：NRF**

该命令用于在NRF新增分层互联通配属性，以减少分层互联路由信息的配置量。

若此命令与ADD NRFTAIRT命令配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 注意事项

- 该命令执行后立即生效。

- 当分层互联属性类型为TAC时，通配的起始位置加通配的长度小于等于6，即MATCHSTART+MATCHLEN<=6。
- 当分层互联属性类型为NFGROUP或SERVINGSCOPE时，通配的起始位置加通配的长度小于等于128，即MATCHSTART+MATCHLEN<=128。
- 当分层互联属性类型为REGIONIDSETID时，通配的起始位置加通配的长度小于等于18，即MATCHSTART+MATCHLEN<=18。
- 当分层互联属性类型为ROUTINGINDICATOR时，通配的起始位置加通配的长度小于等于4，即MATCHSTART+MATCHLEN<=4。
- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 最多可输入128条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| ATTRIBUTE | 属性 | 可选必选说明：必选参数<br>参数含义：该参数用于表示分层互联属性类型。<br>数据来源：全网规划<br>取值范围：<br>- TAC（TAC）<br>- NRFNFGROUP（NFGROUP）<br>- SERVINGSCOPE（SERVINGSCOPE）<br>- REGIONIDSETID（区域标识和集合标识）<br>- ROUTINGINDICATOR（选路指示器）<br>默认值：无<br>配置原则：<br>每种属性最多只能配置一条分层互联通配属性。 |
| MATCHSTART | 起始位置 | 可选必选说明：必选参数<br>参数含义：该参数用于表示通配的起始位置。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是0~127。<br>默认值：无<br>配置原则：无 |
| MATCHLEN | 通配长度 | 可选必选说明：必选参数<br>参数含义：该参数用于表示通配的长度。<br>数据来源：全网规划<br>取值范围：整数类型，取值范围是1~128。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NRFWILDCARDATTR]] · 分层互联通配属性（NRFWILDCARDATTR）

## 使用实例

运营商新增分层互联通配属性信息，达到快速配置NRF路由的效果：针对的通配信息为：NRFNFGROUP中起始位置为0，通配长度为3位的通配信息，执行此命令。

```
ADD NRFWILDCARDATTR: ATTRIBUTE=NRFNFGROUP, MATCHSTART=0, MATCHLEN=3;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加分层互联通配属性（ADD-NRFWILDCARDATTR）_09653194.md`
