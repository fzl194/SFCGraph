---
id: UDG@20.15.2@MMLCommand@RMV PATCH
type: MMLCommand
name: RMV PATCH（删除补丁）
nf: UDG
version: 20.15.2
verb: RMV
object_keyword: PATCH
command_category: 配置类
effect_mode: 立即生效
is_dangerous: true
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 升级维护
status: active
---

# RMV PATCH（删除补丁）

## 功能

![](删除补丁（RMV PATCH）_59103386.assets/notice_3.0-zh-cn.png)

本命令属于高危命令，操作不当会影响系统的正常运行，请谨慎使用并联系华为支持协助操作。

该命令用于当系统中补丁存在问题时，删除系统补丁。

## 注意事项

- 该命令执行后立即生效。
- 该命令会删除系统补丁，无补丁、已加载补丁，已激活补丁，执行该操作的结果都是成功。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。 |

## 操作的配置对象

- [补丁（PATCH）](configobject/UDG/20.15.2/PATCH.md)

## 使用实例

删除系统补丁：

```
RMV PATCH:
SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/删除补丁（RMV-PATCH）_59103386.md`
