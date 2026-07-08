---
id: UNC@20.15.2@MMLCommand@LST VLRFUNCSW
type: MMLCommand
name: LST VLRFUNCSW（查询VLR功能开关）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: VLRFUNCSW
command_category: 查询类
applicable_nf:
- SMSF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- VLR业务管理
- VLR功能开关
status: active
---

# LST VLRFUNCSW（查询VLR功能开关）

## 功能

**适用NF：SMSF**

该命令用于查询VLR的功能开关。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@VLRFUNCSW]] · VLR功能开关（VLRFUNCSW）

## 使用实例

运营商希望查询VLR功能开关，执行如下命令：

```
LST VLRFUNCSW:;
%%LST VLRFUNCSW:;%%
RETCODE = 0  操作成功

结果如下：
------------------------
        VLR用户位置更新时分配TMSI开关  =  打开
        VLR向注册中心注册开关          =  打开
        VLR向HLR强制更新开关            =  打开
        VLR内部统计功能开关             =  打开
        PURGE MS消息开关                 =  打开
        本网用户计费开关                =  打开
        外网用户计费开关                =  打开

(结果个数 = 1)
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-VLRFUNCSW.md`
