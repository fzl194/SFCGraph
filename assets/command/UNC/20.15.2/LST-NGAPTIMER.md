---
id: UNC@20.15.2@MMLCommand@LST NGAPTIMER
type: MMLCommand
name: LST NGAPTIMER（查询N2定时器参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGAPTIMER
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- MM协议参数管理
- 5G移动管理定时器
status: active
---

# LST NGAPTIMER（查询N2定时器参数）

## 功能

**适用NF：AMF**

该命令用于查询N2定时器参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [N2定时器参数（NGAPTIMER）](configobject/UNC/20.15.2/NGAPTIMER.md)

## 使用实例

查询N2定时器参数，执行如下命令：

```
%%LST NGAPTIMER:;%%
RETCODE = 0  操作成功

结果如下
------------------------
基站释放广播会话超时时长(秒)  =  4
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询N2定时器参数（LST-NGAPTIMER）_33431273.md`
