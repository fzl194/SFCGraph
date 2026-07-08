---
id: UNC@20.15.2@MMLCommand@DSP SSHSERRORLOG
type: MMLCommand
name: DSP SSHSERRORLOG（显示SSH服务器的错误日志）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SSHSERRORLOG
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- SSH调测
status: active
---

# DSP SSHSERRORLOG（显示SSH服务器的错误日志）

## 功能

该命令用于查询SSH服务器的错误日志。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [SSH服务器的错误日志（SSHSERRORLOG）](configobject/UNC/20.15.2/SSHSERRORLOG.md)

## 使用实例

查询SSH服务器的错误日志：

```
DSP SSHSERRORLOG:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
    时间  =  2024-02-23, 08:27:24:432
日志信息  =  LogOff. TCP disconnect from client(FD=133, ErrorCode=0x201d), User=HAFG, IP=192.168.0.1, SockId=133, ChId=135339, Trace=StartTime:2024-02-23:08-05-26. snd sshver(0)->rev sshver(0)->snd keyinit(0)->rev keyinit(0)->rev curveinit(0)->snd curv... new glbreq(418)->rev new glbreq(538)->rev new glbreq(658)->rev new glbreq(778)->rev new glbreq(898)->rev new glbreq(1018)->rev new glbreq(1138)->rev new glbreq(1258)->rev chnlclose(1318)->snd discnt(1318)->snd camldiscntreq(1318)->END
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/显示SSH服务器的错误日志（DSP-SSHSERRORLOG）_59103912.md`
