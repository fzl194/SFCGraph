---
id: UNC@20.15.2@MMLCommand@DSP SDRPROCESS
type: MMLCommand
name: DSP SDRPROCESS（查询SDRC中缓存的进程信息）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: SDRPROCESS
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 服务通信管理
- 策略查询
status: active
---

# DSP SDRPROCESS（查询SDRC中缓存的进程信息）

## 功能

该命令用于查询SDRC中缓存的进程信息，若指定进程号则显示特定的进程信息，否则列出所有的进程信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| PROCESSID | 进程ID | 可选必选说明：可选参数<br>参数含义：该参数用于标识实例对应的进程ID。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SDRPROCESS]] · SDRC中缓存的进程信息（SDRPROCESS）

## 使用实例

使用如下命令查询SDRC中缓存的进程信息：

```
%%DSP SDRPROCESS: PROCESSID="vup-pod-010-107-0-165__121__0";%%
RETCODE = 0  操作成功

结果如下
--------
   进程ID  =  vup-pod-010-107-0-165__121__0
 FABRIC TB  =  low:1124
FABRIC TPS  =  sdr:2210930432 external:2210995968
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-SDRPROCESS.md`
