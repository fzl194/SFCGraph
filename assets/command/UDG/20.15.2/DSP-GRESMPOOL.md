---
id: UDG@20.15.2@MMLCommand@DSP GRESMPOOL
type: MMLCommand
name: DSP GRESMPOOL（显示Gresm资源池所有信息）
nf: UDG
version: 20.15.2
verb: DSP
object_keyword: GRESMPOOL
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- 操作维护
- 系统调测
- Gresm调测
status: active
---

# DSP GRESMPOOL（显示Gresm资源池所有信息）

## 功能

该命令用于显示本设备上资源管理池的所有信息。GRESM管理着多个资源池，每个资源池都有其属性，DSP GRESMPOOL命令能用来查看资源池的属性。比如：APP向GRESM申请不到相应资源时，可以用该命令查看资源池中是否还有空闲的资源。

## 注意事项

无。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无。

## 操作的配置对象

- [[configobject/UDG/20.15.2/GRESMPOOL]] · Gresm资源池所有信息（GRESMPOOL）

## 使用实例

显示Gresm资源池所有信息：

```
DSP GRESMPOOL:;
```

```

RETCODE = 0  操作成功。

结果如下
--------
资源池类型    资源总数量    资源池起始编号    资源池结束编号    资源块大小    空闲资源数量    资源池是否可用    完成平滑用户数    用户总数

LABEL         299008        32768             331775            256           299008          可用              0                 0
IID           4194304       1                 4194304           512           4194200         可用              8                 8
SLABEL        32752         16                32767             256           32752           可用              0                 0
(结果个数 = 3)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/显示Gresm资源池所有信息（DSP-GRESMPOOL）_00440785.md`
