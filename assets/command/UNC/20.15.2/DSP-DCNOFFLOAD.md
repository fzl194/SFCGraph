---
id: UNC@20.15.2@MMLCommand@DSP DCNOFFLOAD
type: MMLCommand
name: DSP DCNOFFLOAD（查询DCN迁移状态）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: DCNOFFLOAD
command_category: 查询类
applicable_nf:
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 网络管理
- DCN迁移控制
status: active
---

# DSP DCNOFFLOAD（查询DCN迁移状态）

## 功能

**适用网元：MME**

该命令用于查询DCN迁移的进度信息。

## 注意事项

此命令对类型为“IMSI(IMSI)”的迁移任务不生效。针对类型为“IMSI(IMSI)”的迁移任务，可通过用户跟踪等手段查看迁移进度。

## 权限

manage-ug；system-ug；monitor-ug；visit-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组；G_4，来宾级别命令组

## 参数

无。

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@DCNOFFLOAD]] · DCN迁移任务（DCNOFFLOAD）

## 使用实例

1. 查询DCN迁移的进度信息：DSP DCNOFFLOAD:;
  ```
  %%DSP DCNOFFLOAD:;%%
  RETCODE = 0  执行成功

  输出结果如下：
  ------------
           迁移类型  =  全部用户
       指定IMSI前缀  =  NULL
           迁移状态  =  结束完成
     已经迁移用户数  =  1
  剩余迁移时间(min)  =  0
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/DSP-DCNOFFLOAD.md`
