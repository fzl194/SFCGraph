---
id: UNC@20.15.2@MMLCommand@REQ GENSYNCALLCFGNTF
type: MMLCommand
name: REQ GENSYNCALLCFGNTF（请求生成一个全量同步通知）
nf: UNC
version: 20.15.2
verb: REQ
object_keyword: GENSYNCALLCFGNTF
command_category: 调测类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议
status: active
---

# REQ GENSYNCALLCFGNTF（请求生成一个全量同步通知）

## 功能

该命令有助于生成所有配置同步的通知。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [请求生成一个全量同步通知（GENSYNCALLCFGNTF）](configobject/UNC/20.15.2/GENSYNCALLCFGNTF.md)

## 使用实例

NETCONF模拟配置同步通知：

```
REQ GENSYNCALLCFGNTF:
SERVICEINSTANCE="vnfc"
;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/请求生成一个全量同步通知（REQ-GENSYNCALLCFGNTF）_59103801.md`
