---
id: UNC@20.15.2@MMLCommand@DSP CDRDISTR
type: MMLCommand
name: DSP CDRDISTR（显示Push及Local方式下分发任务状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: CDRDISTR
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
- 话单分发
status: active
---

# DSP CDRDISTR（显示Push及Local方式下分发任务状态）

## 功能

**适用NF：NCG**

该命令用于显示PUSH及LOCAL方式向计费中心（本文档中又称BS（Billing System））传送话单文件时，分发任务的状态。该命令执行后，系统返回相应的分发任务状态值。

在系统新安装时、系统调测或者话单分发异常时，可以使用该命令进行检查。

查询方式有4种：

不输入参数，查询所有话单分发任务。

输入“分发任务标识”参数，查询指定分发任务标识所涉及话单分发任务。

输入“接入网元分组标识”参数，查询指定接入网元分组上所有话单分发任务。

输入“模块名”参数，查询模块名上所有话单分发任务。

## 注意事项

该命令在单个RU上最多支持查询大约2400条链路信息，超过会出现“操作超时”，建议查询时输入“分发任务标识”参数。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CDRDISTRID | 分发任务标识 | 可选必选说明：可选参数<br>参数含义：分发任务标识，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |
| MNAME | 模块名 | 可选必选说明：可选参数<br>参数含义：用于标识一个业务模块对象，全局唯一。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～15。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@CDRDISTR]] · 上传SFTP密钥文件到BS侧（CDRDISTR）

## 使用实例

显示所有分发任务状态：

```
DSP CDRDISTR: CDRDISTRID="dispush";
```

```
RETCODE = 0  操作成功。

结果如下:
------------------------
    分发任务标识  =  dispush
接入网元分组标识  =  ps1
          模块名  =  AP66_1
        通道列表  =  AP66_1/flatrate
     NCG侧IP地址  =  192.168.1.7
      BS侧IP地址  =  192.168.1.1
  BS侧控制端口号  =  22
        任务状态  =  等待
日志稽核功能状态  =  未启用
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-CDRDISTR.md`
