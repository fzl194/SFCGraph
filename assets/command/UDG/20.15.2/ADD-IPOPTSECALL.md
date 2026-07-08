---
id: UDG@20.15.2@MMLCommand@ADD IPOPTSECALL
type: MMLCommand
name: ADD IPOPTSECALL（添加IP全局选项安全配置）
nf: UDG
version: 20.15.2
verb: ADD
object_keyword: IPOPTSECALL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
max_records: 1
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP选项全局安全配置
status: active
---

# ADD IPOPTSECALL（添加IP全局选项安全配置）

## 功能

该命令用于添加IP全局选项安全配置。

通常情况下带路由选项的IP报文用于网络路径的故障诊断和特殊业务的临时传送。但是路由选项可能被网络攻击者利用，探测网络结构并发动攻击。

为了提高安全性，防止系统收到特定报文的攻击，系统可以对带路由选项的IP报文配置全局过滤策略，丢弃报文或正常处理。

如果需要配置单独路由选项过滤规则，请使用SET IPOPTSECURITY进行配置。

当全局过滤策略和单独路由选项过滤策略不一致时，有错误提示信息"选项不一致"。

## 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCHOP | IP过滤规则 | 可选必选说明：必选参数<br>参数含义：该参数表明IP全局报文过滤规则状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/IPOPTSECALL]] · IP全局选项安全配置（IPOPTSECALL）

## 使用实例

添加IP全局选项安全配置：

```
ADD IPOPTSECALL:SWITCHOP=deny;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/添加IP全局选项安全配置（ADD-IPOPTSECALL）_00840613.md`
