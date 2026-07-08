---
id: UNC@20.15.2@MMLCommand@DSP PFCPSESSMIGSTS
type: MMLCommand
name: DSP PFCPSESSMIGSTS（显示PFCP会话迁移任务状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: PFCPSESSMIGSTS
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
- 接口管理
- PFCP接口管理
- PFCP路径管理
- PFCP会话迁移状态查询
status: active
---

# DSP PFCPSESSMIGSTS（显示PFCP会话迁移任务状态）

## 功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询PFCP会话迁移任务状态。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MIGTYPE | 迁移类型 | 可选必选说明：可选参数<br>参数含义：该参数用于指定迁移类型。<br>数据来源：本端规划<br>取值范围：<br>- UPF（指定UPF）<br>- IMSISEG（指定IMSI号段）<br>默认值：UPF<br>配置原则：无 |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：该参数在"MIGTYPE"配置为"UPF"时为条件可选参数。<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~36。不区分大小写。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@PFCPSESSMIGSTS]] · PFCP会话迁移任务状态（PFCPSESSMIGSTS）

## 使用实例

- 当希望查询upf1的搬迁状态时，使用如下命令：
  ```
  %%DSP PFCPSESSMIGSTS:MIGTYPE=UPF,NFINSTANCENAME="upf";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         执行阶段  =  当前迁移任务待启动
      迁移进度(%)  =  0
   剩余迁移会话数  =  0
     迁移开始时间  =  NULL
     迁移结束时间  =  NULL
       迁移源路径  =  192.168.0.1
     迁移目的路径  =  192.168.0.2
     待启动的列表  =  NULL
       完成的列表  =  NULL
       运行的列表  =  NULL
       停止的列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 当希望查询全部upf的搬迁状态时，使用如下命令：
  ```
  %%DSP PFCPSESSMIGSTS:MIGTYPE=UPF;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
         执行阶段  =  当前迁移任务待启动
      迁移进度(%)  =  0
   剩余迁移会话数  =  0
     迁移开始时间  =  NULL
     迁移结束时间  =  NULL
       迁移源路径  =  0.0.0.0
     迁移目的路径  =  NULL
     待启动的列表  =  upf1, upf2
       完成的列表  =  NULL
       运行的列表  =  NULL
       停止的列表  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-PFCPSESSMIGSTS.md`
