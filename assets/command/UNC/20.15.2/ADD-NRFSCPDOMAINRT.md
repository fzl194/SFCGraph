---
id: UNC@20.15.2@MMLCommand@ADD NRFSCPDOMAINRT
type: MMLCommand
name: ADD NRFSCPDOMAINRT（增加SCP Domain最长匹配后缀转发路由）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: NRFSCPDOMAINRT
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
- SCP Domain路由管理
status: active
---

# ADD NRFSCPDOMAINRT（增加SCP Domain最长匹配后缀转发路由）

## 功能

**适用NF：NRF**

该命令用于新增基于SCP Domain的最长匹配后缀的转发路由。当跨NRF对某个NF进行寻址时，通过本命令配置的信息可以找到当前NRF的下一级NRF路由，即目标NF所归属的NRF。

如果针对同一个SCP Domain配置了多个不同的下一跳归属NRF组名称，那么当前NRF会选取下一跳所有归属NRF组中优先级最高的NRF。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SCPDOMAINSUFFIX | SCP Domain后缀 | 可选必选说明：必选参数<br>参数含义：该参数用于表示SCP Domain后缀。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：无 |
| NEXTNRFGRPNAME | 归属NRF组名称 | 可选必选说明：必选参数<br>参数含义：该参数用于表示当前NRF基于SCP domain的最长后缀匹配寻址NF时的下一跳NRF实例组名称，即被寻址的NF归属于该NRF实例组。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~64。<br>默认值：无<br>配置原则：<br>该参数已通过ADD NRFGROUP配置，可通过LST NRFGROUP命令查询获取。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NRFSCPDOMAINRT]] · SCP Domain最长匹配后缀转发路由（NRFSCPDOMAINRT）

## 使用实例

增加一条SCP Domain后缀为32123ASDF，归属NRF组名称为azh0701的最长匹配后缀的转发路由配置，执行如下命令：

```
ADD NRFSCPDOMAINRT: SCPDOMAINSUFFIX="32123ASDF", NEXTNRFGRPNAME="azh0701";
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/ADD-NRFSCPDOMAINRT.md`
