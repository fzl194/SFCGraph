---
id: UNC@20.15.2@MMLCommand@LST DNNCMPT
type: MMLCommand
name: LST DNNCMPT（查询DNN兼容性控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNNCMPT
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NAS传输管理
- DNN兼容性控制管理
status: active
---

# LST DNNCMPT（查询DNN兼容性控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF与周边NF交互时的DNN相关控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNCMPT]] · DNN兼容性控制参数（DNNCMPT）

## 使用实例

查询AMF上当前配置的DNN兼容性控制参数，执行如下命令：

```
%%LST DNNCMPT:;%%
RETCODE = 0  操作成功

结果如下
------------------------
          本网用户DNN格式  =  仅网络标识
       LBO漫游用户DNN格式  =  完整DNN
        HR漫游用户DNN格式  =  完整DNN
     AMF间本网用户DNN格式  =  仅网络标识
AMF间LBO漫游会话的DNN格式  =  完整DNN
   AMF间HR漫游会话DNN格式  =  完整DNN
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNN兼容性控制参数（LST-DNNCMPT）_96242127.md`
