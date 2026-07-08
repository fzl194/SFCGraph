---
id: UNC@20.15.2@MMLCommand@DSP ACTRL
type: MMLCommand
name: DSP ACTRL（显示CGF与对端网元链路状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: ACTRL
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
- 接入控制
status: active
---

# DSP ACTRL（显示CGF与对端网元链路状态）

## 功能

**适用NF：NCG**

该命令用于显示CGF与对端之间的链路状态。该命令执行后，系统会显示CGF与对端之间链路状态。

当系统新安装、日常维护或者CG不能从CGF接收话单时，可以使用该命令。

## 注意事项

该命令查询到的是实时的链路状态。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| AGID | 接入网元分组标识 | 可选必选说明：可选参数<br>参数含义：用于区分不同域的接入网元。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围为1～32。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@ACTRL]] · 接入控制（ACTRL）

## 使用实例

查询PS域网元所有CGF与对端链路状态，示例如下：

```
DSP ACTRL:;
```

```
RETCODE = 0  操作成功。

结果如下:
--------
    接入控制标识  =  ACID_1
接入网元分组标识  =  ps1
       CG IP地址  =  192.168.17.177
        CG端口号  =  3386
       Ga IP地址  =  192.168.17.17
        Ga端口号  =  5001
      AP模块编号  =  641
        链路状态  =  正常
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-ACTRL.md`
