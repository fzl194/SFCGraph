---
id: UNC@20.15.2@MMLCommand@LST AMFNASFIXEDFC
type: MMLCommand
name: LST AMFNASFIXEDFC（查询指定消息类型的AMF NAS固定速率流控信息）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: AMFNASFIXEDFC
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 移动性管理
- 拥塞控制
- AMF NAS固定速率流控
status: active
---

# LST AMFNASFIXEDFC（查询指定消息类型的AMF NAS固定速率流控信息）

## 功能

**适用NF：AMF**

该命令用于查询指定消息类型的AMF NAS固定速率流控信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| MSGTYPE | 流控消息类型 | 可选必选说明：可选参数<br>参数含义：该参数用于设置AMF被流控的NAS消息类型。<br>数据来源：全网规划<br>取值范围：<br>- PDUSESSIONEST（PDU Session Establishment Request）<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/AMFNASFIXEDFC]] · 指定消息类型的AMF NAS固定速率流控信息（AMFNASFIXEDFC）

## 使用实例

查询所有流控消息类型流控信息，执行如下命令：

```
%%LST AMFNASFIXEDFC:;%%
RETCODE = 0  操作成功

结果如下
------------------------
             流控消息类型  =  PDUSESSIONEST
         固定速率流控开关  =  打开
      流控速率门限(个/秒)  =  1000
         流控阈值作用范围  =  单usn-pod
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-AMFNASFIXEDFC.md`
