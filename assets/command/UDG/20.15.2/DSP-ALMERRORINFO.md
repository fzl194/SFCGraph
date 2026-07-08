---
id: UDG@20.15.2@MMLCommand@DSP ALMERRORINFO
type: MMLCommand
name: DSP ALMERRORINFO（查询告警模块错误信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: ALMERRORINFO
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 操作维护
- 系统调测
- 告警管理调测
status: active
---

# DSP ALMERRORINFO（查询告警模块错误信息）

## 功能

该命令用于查询告警模块错误信息。告警模块处理异常出错信息会记入缓存，用户可通过该命令查询缓存内容，缓存内容可协助用户定位告警上报失败或其它业务处理失败的原因。缓存内容重启会丢失。

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

- [告警模块错误信息（ALMERRORINFO）](configobject/UDG/20.15.2/ALMERRORINFO.md)

## 使用实例

查询告警模块错误信息：

```
DSP ALMERRORINFO:
SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

结果如下
-------------------------
告警模块错误信息

2017-02-24 08:49:30.684 Add fom ntf info to dictionary failed, alarm fim id = 0x81300af
2017-02-24 08:49:30.684 Add fom ntf info to dictionary failed, alarm fim id = 0x813215d
2017-02-24 08:49:30.684 Add fom ntf info to dictionary failed, alarm fim id = 0x813218d
2017-02-24 08:49:30.684 Add fom ntf info to dictionary failed, alarm fim id = 0x813215c
2017-02-24 08:49:31.516 Get MML user info error                                     
(结果个数 = 5)
--- END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/查询告警模块错误信息（DSP-ALMERRORINFO）_59103821.md`
