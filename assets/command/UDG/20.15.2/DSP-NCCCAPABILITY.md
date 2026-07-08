---
id: UDG@20.15.2@MMLCommand@DSP NCCCAPABILITY
type: MMLCommand
name: DSP NCCCAPABILITY（查询设备所支持的NETCONFC协议能力集）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: NCCCAPABILITY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议客户端
status: active
---

# DSP NCCCAPABILITY（查询设备所支持的NETCONFC协议能力集）

## 功能

该命令用于查询设备所支持的NETCONFC协议能力集。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [设备所支持的NETCONFC协议能力集（NCCCAPABILITY）](configobject/UDG/20.15.2/NCCCAPABILITY.md)

## 使用实例

查询设备所支持的NETCONFC协议能力集：

```
DSP NCCCAPABILITY:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
能力集名称           能力集类型  能力集版本  组件PID

Action                private     1.0      0x1970022
Action                private     2.0      0x1970022
Base                  public      1.0      0x1970022
Base                  private     2.0      0x1970022
Distinct Startup      public      1.0      0x1970022
Exchange              private     1.0      0x1970022
Sync-Config           private     1.0      0x1970022
Writable-Running      public      1.0      0x1970022
Weak-Checking         private     1.0      0x1970022
(结果个数 = 9)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询设备所支持的NETCONFC协议能力集（DSP-NCCCAPABILITY）_59103534.md`
