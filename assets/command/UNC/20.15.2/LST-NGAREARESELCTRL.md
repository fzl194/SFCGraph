---
id: UNC@20.15.2@MMLCommand@LST NGAREARESELCTRL
type: MMLCommand
name: LST NGAREARESELCTRL（查询AMF区域重选功能控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: NGAREARESELCTRL
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- AMF区域重选功能管理
- AMF区域重选控制
status: active
---

# LST NGAREARESELCTRL（查询AMF区域重选功能控制参数）

## 功能

**适用NF：AMF**

该命令用于查询AMF区域重选功能控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [AMF区域重选功能控制参数（NGAREARESELCTRL）](configobject/UNC/20.15.2/NGAREARESELCTRL.md)

## 使用实例

查询AMF区域重选功能控制参数，执行如下命令：

```
%%LST NGAREARESELCTRL:;%%
RETCODE = 0  操作成功。

输出结果如下
------------------------
    区域重路由开关  =  开启
    重复重路由开关  =  关闭
重路由语音优先开关  =  开启
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询AMF区域重选功能控制参数（LST-NGAREARESELCTRL）_23622946.md`
