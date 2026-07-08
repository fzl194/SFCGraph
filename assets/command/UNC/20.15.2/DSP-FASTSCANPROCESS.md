---
id: UNC@20.15.2@MMLCommand@DSP FASTSCANPROCESS
type: MMLCommand
name: DSP FASTSCANPROCESS（显示快速扫描任务状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: FASTSCANPROCESS
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
- SMF
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 快速扫描任务管理
status: active
---

# DSP FASTSCANPROCESS（显示快速扫描任务状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示快速扫描任务状态。

## 注意事项

- 当参数“循环扫描任务”为true时，表示该扫描任务为循环任务，查询命令时不显示参数“预期结束时间”和参数“进度（%）”。
- 当扫描任务结束后，执行DSP FASTSCANPROCESS不返回结果。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| TASKTYPE | 扫描任务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定扫描任务类型。<br>数据来源：本端规划<br>取值范围：<br>- UPF_DEACTIVE（UPF去活扫描任务）<br>- SBC_FAULT（SBC故障扫描任务）<br>默认值：无<br>配置原则：无 |
| TASKINSTNAME | 扫描对象实例名 | 可选必选说明：可选参数<br>参数含义：该参数用于表示扫描任务对象实例名。不区分大小写。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是0~1024。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@FASTSCANPROCESS]] · 快速扫描任务状态（FASTSCANPROCESS）

## 使用实例

查询系统中TASKTYPE=UPF_DEACTIVE的快速扫描任务状态：

```
%%DSP FASTSCANPROCESS: TASKTYPE=UPF_DEACTIVE;%%
RETCODE = 0  操作成功

结果如下
------------------------
  扫描任务类型  =  UPF去活扫描任务
扫描对象实例名  =  upf_instance_1
    微服务名称  =  UpcCtrlSvc
      扫描速率  =  200
  循环扫描任务  =  FALSE
      启动时间  =  2024-11-11 09:00:00
  预期结束时间  =  2024-11-11 16:00:00
     进度（%）  =  85
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-FASTSCANPROCESS.md`
