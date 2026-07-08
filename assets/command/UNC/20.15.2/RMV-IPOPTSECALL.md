---
id: UNC@20.15.2@MMLCommand@RMV IPOPTSECALL
type: MMLCommand
name: RMV IPOPTSECALL（删除IP全局选项安全配置）
nf: UNC
version: 20.15.2
verb: RMV
object_keyword: IPOPTSECALL
command_category: 配置类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- IP协议栈
- IPv4管理
- IP选项全局安全配置
status: active
---

# RMV IPOPTSECALL（删除IP全局选项安全配置）

## 功能

该命令用于删除IP全局选项安全配置。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SWITCHOP | IP过滤规则 | 可选必选说明：必选参数<br>参数含义：该参数表明IP全局报文过滤规则状态。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- permit：允许。<br>- deny：拒绝。<br>默认值：无 |

## 操作的配置对象

- [IP全局选项安全配置（IPOPTSECALL）](configobject/UNC/20.15.2/IPOPTSECALL.md)

## 使用实例

删除IP全局选项安全配置：

```
RMV IPOPTSECALL:SWITCHOP=permit;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/删除IP全局选项安全配置（RMV-IPOPTSECALL）_00601105.md`
