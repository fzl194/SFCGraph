---
id: UNC@20.15.2@MMLCommand@DSP SSHCERRORLOG
type: MMLCommand
name: DSP SSHCERRORLOG（显示SSH客户端的错误日志）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SSHCERRORLOG
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

# DSP SSHCERRORLOG（显示SSH客户端的错误日志）

## 功能

该命令用于查询SSH客户端的错误日志。

## 注意事项

无。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过<br>**LST VNFC**<br>命令获取。<br>默认值：无<br>配置原则：只能填写通过<br>**LST VNFC**<br>命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/SSHCERRORLOG]] · SSH客户端的错误日志（SSHCERRORLOG）

## 使用实例

查询SSH客户端的错误日志：

```
DSP SSHCERRORLOG:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
    时间  =  2016-08-04, 20:45:32:445
日志信息  =  Session disconnected.(ServiceType=stelnet, UserName=Could not extract user name, IPAddress=10.179.175.55, FailedReason=SSH connection was aborted by user.)
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SSHCERRORLOG.md`
