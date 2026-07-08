---
id: UNC@20.15.2@MMLCommand@DSP S1BALANCE
type: MMLCommand
name: DSP S1BALANCE（查询S1接口均衡操作结果）
nf: UNC
version: 20.15.2
verb: DSP
object_keyword: S1BALANCE
command_category: 查询类
applicable_nf:
- MME
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- S1接口管理
- S1接口均衡管理
status: active
---

# DSP S1BALANCE（查询S1接口均衡操作结果）

## 功能

**适用网元：MME**

此命令用于查询当前S1接口均衡操作的结果。

## 注意事项

- 此命令执行后立即生效。
- 在迁移过程中执行此命令，可以查询当前S1接口均衡操作的进度。
- 在迁移结束后执行此命令，可以查询执行此命令前最后一次S1接口均衡操作的执行结果。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UNC/20.15.2/S1BALANCE]] · S1接口均衡操作（S1BALANCE）

## 使用实例

1. 查询S1接口均衡操作结果：
  DSP S1BALANCE:;
  ```
  %%DSP S1BALANCE:;%%
  RETCODE = 0  操作成功。

  操作结果如下
  -------------------------
              迁移范围  =  系统自动均衡迁移
              迁移状态  =  迁移中 
  需要迁移的eNodeB总数  =  500  
    迁移成功的eNodeB数  =  377
    迁移失败的eNodeB数  =  77
  (结果个数 = 1)

   ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询S1接口均衡操作结果(DSP-S1BALANCE)_26146240.md`
