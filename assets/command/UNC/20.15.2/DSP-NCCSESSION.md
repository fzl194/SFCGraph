---
id: UNC@20.15.2@MMLCommand@DSP NCCSESSION
type: MMLCommand
name: DSP NCCSESSION（显示NETCONFC会话信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCCSESSION
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 网络配置协议客户端
status: active
---

# DSP NCCSESSION（显示NETCONFC会话信息）

## 功能

该命令用于显示NETCONFC会话信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/NCCSESSION]] · NETCONFC会话信息（NCCSESSION）

## 使用实例

显示NETCONFC会话信息：

```
DSP NCCSESSION:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
-------------------------
远端ID     NETCONFC会话ID         用户名             会话类型        状态     会话成功建立的时间     组件PID

1026       316                    OMO_VNFC_SYSTEM    CFG             READY    2018-05-08 21:36:15    0x197002e    
1025       317                    OMO_VNFC_SYSTEM    CFG             READY    2018-05-08 21:36:15    0x1970024  
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCCSESSION.md`
