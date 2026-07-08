---
id: UNC@20.15.2@MMLCommand@LST CDRPROC
type: MMLCommand
name: LST CDRPROC（查询话单处理）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: CDRPROC
command_category: 查询类
applicable_nf:
- NCG
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- NCG业务及策略管理
- 计费管理
- 业务配置管理
- 话单处理
status: active
---

# LST CDRPROC（查询话单处理）

## 功能

**适用NF：NCG**

该命令用于查询当前系统的格式引擎包信息。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| PRFNAME | 格式引擎包名 | 可选必选说明：可选参数<br>参数含义：格式引擎包定义了CG话单处理的业务规则，主要包括话单字段过滤配置、分拣条件配置、通道配置、话单处理脚本等。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～255。<br>默认值：无<br>配置原则：无 |
| CDRTIMEOUT | 话单超时时间（分钟） | 可选必选说明：可选参数<br>参数含义：表示话单合并过程中能容许的超时时间。<br>数据来源：对端协商<br>取值范围：整数类型，取值范围为0～14400，单位是分钟。<br>默认值：无<br>配置原则：无 |
| SHAREFILECSN | 共享第二份最终话单文件序列号 | 可选必选说明：可选参数<br>参数含义：用于设置共享第二份最终话单文件序列号功能关闭或开启。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- OFF：关闭。<br>- ON：开启。<br>默认值：无<br>配置原则：无 |
| SEQNUMMODE | 序列号模式 | 可选必选说明：可选参数<br>参数含义：控制NCG回复的Cancel response和Release response的IE中携带的Sequence number来自GSN发送的Cancel request或Release request的gtp'帧的Head还是IE。<br>数据来源：本端规划<br>取值范围：枚举类型。<br>- IE：序列号源自gtp'的IE。<br>- HEAD：序列号源自gtp'的Head。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/CDRPROC]] · 话单处理（CDRPROC）

## 使用实例

查询CG系统当前使用的话单处理配置：

```
LST CDRPROC:;
```

```
RETCODE = 0  操作成功。

结果如下:
---------
            接入网元分组标识  =  PS_GROUP_1
                格式引擎包名  =  PS_R9_V940_NM_RT.tar.gz
        话单超时时间（分钟）  =  1440
共享第二份最终话单文件序列号  =  关闭
                  序列号模式  =  序列号源自gtp'的IE
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询话单处理（LST-CDRPROC）_51174275.md`
