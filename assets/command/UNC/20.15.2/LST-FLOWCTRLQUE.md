---
id: UNC@20.15.2@MMLCommand@LST FLOWCTRLQUE
type: MMLCommand
name: LST FLOWCTRLQUE（查询流控队列信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: FLOWCTRLQUE
command_category: 查询类
applicable_nf:
- SGSN
- MME
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- Pre 5G接入业务管理
- 控制面管理
- 操作维护
- 设备管理
- 流控管理
- 系统流控队列管理
status: active
---

# LST FLOWCTRLQUE（查询流控队列信息）

## 功能

**适用网元：SGSN、MME**

该命令用于显示不同业务类型的流控队列。

## 注意事项

无。

## 权限

manage-ug；system-ug；monitor-ug
G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| APPTYPE | 业务类型 | 可选必选说明：必选参数<br>参数含义：该参数用于指定业务类型。<br>取值范围：<br>- “APP_2G(2G)”：表示2G业务类型。<br>- “APP_3G(3G)”：表示3G业务类型。<br>- “APP_4G(4G)”：表示4G业务类型。<br>默认值：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/FLOWCTRLQUE]] · 流控队列信息（FLOWCTRLQUE）

## 使用实例

显示流控队列信息：

LST FLOWCTRLQUE: APPTYPE=APP_2G;

```
%%LST FLOWCTRLQUE: APPTYPE=APP_2G;%%
RETCODE = 0  操作成功。

输出结果如下
-------------------------
业务类型  消息类型   业务权重  队列期望长度

 2G        ATTACH     4         400         
 2G        RAU        4         400         
 2G        PDP_ACT    9         400         
(结果个数 = 3)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-FLOWCTRLQUE.md`
