---
id: UNC@20.15.2@MMLCommand@LST NCCPOLICY
type: MMLCommand
name: LST NCCPOLICY（查询NCC策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NCCPOLICY
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- 操作维护
- 配置服务管理
- 维护管理
status: active
---

# LST NCCPOLICY（查询NCC策略）

## 功能

该命令用于查询NCC策略。

## 注意事项

无。

## 参数

无。

## 操作的配置对象

- [NCC策略（NCCPOLICY）](configobject/UNC/20.15.2/NCCPOLICY.md)

## 使用实例

查询NCC策略时，执行以下命令：

```
%%LST NCCPOLICY:;%% 
RETCODE = 0  操作成功  

操作结果如下 
------------ 
策略标识  =  内存优化开关策略 
策略内容  =  关闭 
(结果个数 = 1)  

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询NCC策略(LST-NCCPOLICY)_69362704.md`
