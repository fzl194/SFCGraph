---
id: UNC@20.15.2@MMLCommand@LST SMFCACHEFUNC
type: MMLCommand
name: LST SMFCACHEFUNC（查询SMF映射关系的本地缓存策略）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SMFCACHEFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- NF发现和选择管理
- SMF缓存策略管理
status: active
---

# LST SMFCACHEFUNC（查询SMF映射关系的本地缓存策略）

## 功能

**适用NF：AMF**

该命令用于查询当前配置的SMF映射关系的本地缓存策略。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@SMFCACHEFUNC]] · SMF映射关系的本地缓存策略（SMFCACHEFUNC）

## 使用实例

查询SMF映射关系缓存策略，执行如下命令：

```
%%LST SMFCACHEFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
           是否打开SMF映射关系本地缓存  =  否
                        老化时长(分钟)  =  4
          45G互操作场景是否打开SMF缓存  =  是
  非漫游AMF内移动性流程是否打开SMF缓存  =  是
漫游场景AMF内移动性流程是否打开SMF缓存  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-SMFCACHEFUNC.md`
