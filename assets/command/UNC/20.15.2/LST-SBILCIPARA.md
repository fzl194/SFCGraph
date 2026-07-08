---
id: UNC@20.15.2@MMLCommand@LST SBILCIPARA
type: MMLCommand
name: LST SBILCIPARA（查询服务化接口负载控制参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SBILCIPARA
command_category: 查询类
applicable_nf:
- AMF
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- 服务化接口管理
- 注册与服务发现
- 负载控制信息管理
status: active
---

# LST SBILCIPARA（查询服务化接口负载控制参数）

## 功能

**适用NF：AMF、SMF**

该命令用于查询服务化接口负载控制参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [服务化接口负载控制参数（SBILCIPARA）](configobject/UNC/20.15.2/SBILCIPARA.md)

## 使用实例

查询服务化接口负载控制参数：

```
%%LST SBILCIPARA:;%%
RETCODE = 0  操作成功

结果如下
--------
服务化接口负载控制开关  =  关
       负载通知阈值(%)  =  80
       负载通知步长(%)  =  5
负载获取间隔时长(分钟)  =  5
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询服务化接口负载控制参数（LST-SBILCIPARA）_46692903.md`
