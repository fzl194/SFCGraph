---
id: UNC@20.15.2@MMLCommand@DSP LOGERRORINFO
type: MMLCommand
name: DSP LOGERRORINFO（查询日志模块错误信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: LOGERRORINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 日志管理调测
status: active
---

# DSP LOGERRORINFO（查询日志模块错误信息）

## 功能

该命令用于查询日志模块错误信息。日志模块处理异常出错信息会记入缓存，用户可通过该命令查询缓存内容，缓存内容可协助用户定位日志记入文件失败或日志上报网管失败等问题的失败原因。缓存内容重启会丢失。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MASTERORSLAVE | 主备OMU标识 | 可选必选说明：可选参数<br>参数含义：主备OMU标识。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- MASTER：主主控。<br>- SLAVE：备主控。<br>默认值：MASTER |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [日志模块错误信息（LOGERRORINFO）](configobject/UNC/20.15.2/LOGERRORINFO.md)

## 使用实例

查询日志模块错误信息：

```
DSP LOGERRORINFO:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
日志模块错误信息

2017-02-18 07:56:27.764 E:Out put trap buffer failed with error code:0x1                                                     
2017-02-18 07:56:27.764 E:Out put info[0x8151035] to netconf, notification dic not exist[vsMngId=0]!              
2017-02-18 07:56:30.461 E:Log para err.(logid=0x8301007, appParaNum=0, dicParaNum=1)                                         
2017-02-18 07:56:30.461 E:Log para err.(logid=0x8301007, appParaNum=0, dicParaNum=1)                                         
(结果个数 = 4)
--- END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询日志模块错误信息（DSP-LOGERRORINFO）_59104178.md`
