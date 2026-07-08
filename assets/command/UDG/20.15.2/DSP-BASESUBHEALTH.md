---
id: UDG@20.15.2@MMLCommand@DSP BASESUBHEALTH
type: MMLCommand
name: DSP BASESUBHEALTH（显示base链路亚健康信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: BASESUBHEALTH
command_category: 查询类
effect_mode: 立即生效
is_dangerous: false
category_path:
- 平台服务管理
- 单体服务公共功能管理
- 系统管理
- 资源管理
- RU管理
status: active
---

# DSP BASESUBHEALTH（显示base链路亚健康信息）

## 功能

该命令用于显示base链路亚健康信息。

## 注意事项

该命令执行后立即生效。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SRCRUNAME | 本端RU名 | 可选必选说明：必选参数<br>参数含义：本端RU名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，不支持空格。<br>默认值：无 |
| DSTRUNAME | 对端RU名 | 可选必选说明：可选参数<br>参数含义：对端RU名。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～63，不支持空格。<br>默认值：无 |
| SERVICEINSTANCE | 服务实例 | 可选必选说明：必选参数<br>参数含义：该参数表示大颗粒服务实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，通过LST VNFC命令获取，不支持空格。<br>默认值：无<br>配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

## 操作的配置对象

- [[configobject/UDG/20.15.2/BASESUBHEALTH]] · base链路亚健康信息（BASESUBHEALTH）

## 使用实例

显示base链路亚健康信息：

```
DSP BASESUBHEALTH:SRCRUNAME="VNODE_CSLB_VNFC_OMU_0001"
,SERVICEINSTANCE="vnfc"
;
```

```
RETCODE = 0  操作成功

查询base面通信亚健康
------------------------
本端RU名称                  对端RU名称                   平面序号           通道序号       是否激活         源MAC                 目的MAC              是否亚健康      丢包率（千分比）  错包率（千分比）    亚健康值（千分比）    平均时延（微秒）  最大时延（微秒）    最小时延（微秒）

VNODE_CSLB_VNFC_OMU_0001    VNODE_CSLB_VNFC_OMU_0002     0                  0              TRUE             00-e0-fc-13-26-39     00-e0-fc-27-48-92    FALSE           0                  0                   0                    678               1020                300
VNODE_CSLB_VNFC_OMU_0001    VNODE_CSLB_VNFC_SPU_0065     0                  0              TRUE             00-e0-fc-13-26-39     00-e0-fc-27-48-92    FALSE           0                  0                   0                    680               1050                305
(结果个数 = 2)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/DSP-BASESUBHEALTH.md`
