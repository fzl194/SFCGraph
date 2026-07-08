---
id: UNC@20.15.2@MMLCommand@LST DNNREPLACEFUNC
type: MMLCommand
name: LST DNNREPLACEFUNC（查询DNN替换功能管理参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: DNNREPLACEFUNC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- DNN替换功能管理
status: active
---

# LST DNNREPLACEFUNC（查询DNN替换功能管理参数）

## 功能

**适用NF：AMF**

此命令用于查询DNN替换功能管理参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/DNNREPLACEFUNC]] · DNN替换功能管理参数（DNNREPLACEFUNC）

## 使用实例

查询DNN替换功能管理参数，执行如下命令：

```
%%LST DNNREPLACEFUNC:;%%
RETCODE = 0  操作成功

结果如下
--------
DNN替换功能开关  =  是
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询DNN替换功能管理参数（LST-DNNREPLACEFUNC）_23622934.md`
