---
id: UDG@20.15.2@MMLCommand@DSP NCSNTFSTC
type: MMLCommand
name: DSP NCSNTFSTC（显示NETCONF通知会话的统计信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NCSNTFSTC
command_category: 查询类
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

# DSP NCSNTFSTC（显示NETCONF通知会话的统计信息）

## 功能

该命令用于显示NETCONF通知会话的统计信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SESSIONID | 会话ID | 可选必选说明：可选参数<br>参数含义：NETCONF会话标识。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围为1～65535。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/NCSNTFSTC]] · NETCONF通知会话的统计信息（NCSNTFSTC）

## 使用实例

显示NETCONF通知会话的统计信息：

```
DSP NCSNTFSTC:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
          会话ID  =  208
    接收告警个数  =  0
发送的告警通知数  =  0
    认证丢弃个数  =  0
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-NCSNTFSTC.md`
