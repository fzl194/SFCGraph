---
id: UNC@20.15.2@MMLCommand@LST SMFFUNCTION
type: MMLCommand
name: LST SMFFUNCTION（查询SMF功能实例信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFFUNCTION
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 性能统计管理
- SMF性能对象管理
status: active
---

# LST SMFFUNCTION（查询SMF功能实例信息）

## 功能

**适用NF：SMF**

本命令用于查询SMF功能实例信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/SMFFUNCTION]] · SMF功能实例信息（SMFFUNCTION）

## 使用实例

查询所有SMF功能实例的配置信息:

```
LST SMFFUNCTION:;
%%LST SMFFUNCTION:;%%
RETCODE = 0  执行成功

结果如下
------------------------
           NF功能实体号  =  Instanceid01
         NF功能实体描述  =  nfdescription02
               管理状态  =  Locked
               运行状态  =  Enabled
                   FQDN  =  fqdn02
          最大PDU会话数  =  0
              最大QFI数  =  0
(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFFUNCTION.md`
