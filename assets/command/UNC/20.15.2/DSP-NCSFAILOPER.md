---
id: UNC@20.15.2@MMLCommand@DSP NCSFAILOPER
type: MMLCommand
name: DSP NCSFAILOPER（显示操作失败信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: NCSFAILOPER
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

# DSP NCSFAILOPER（显示操作失败信息）

## 功能

该命令用于显示操作失败信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BOARDTYPE | OMU类型 | 可选必选说明：可选参数<br>参数含义：OMU类型。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- master：主OMU。<br>- slave：备OMU。<br>默认值：master |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@NCSFAILOPER]] · 操作失败信息（NCSFAILOPER）

## 使用实例

显示操作失败信息：

```
DSP NCSFAILOPER:BOARDTYPE=master
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下:
------------------------
NETCONF会话ID  =  64
       时间戳  =  2016-08-04, 10:43:22:451
     错误信息  =  Invalid RPC request.;Oper=unknown;MsgId=.
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-NCSFAILOPER.md`
