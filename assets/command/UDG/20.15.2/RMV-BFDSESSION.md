---
id: UDG@20.15.2@MMLCommand@RMV BFDSESSION
type: MMLCommand
name: RMV BFDSESSION（删除BFD会话）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: BFDSESSION
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- BFD管理
- BFD会话
status: active
---

# RMV BFDSESSION（删除BFD会话）

## 功能

![](删除BFD会话（RMV BFDSESSION）_00600649.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会使依赖BFD检测的业务无法通过BFD快速感知故障，请谨慎使用并联系华为技术支持协助操作。

该命令用于删除BFD静态会话配置。

## 注意事项

- 该命令执行后立即生效。
- 对于依赖BFD检测的业务将无法通过BFD快速感知故障。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSNAME | 会话名称 | 可选必选说明：必选参数<br>参数含义：会话名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～64。不区分大小写，不支持空格。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BFDSESSION]] · BFD会话参数（BFDSESSION）

## 使用实例

删除名为Huawei123的BFD会话：

```
RMV BFDSESSION:SESSNAME="Huawei123";
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除BFD会话（RMV-BFDSESSION）_00600649.md`
