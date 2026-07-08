---
id: UNC@20.15.2@MMLCommand@LST STGTRIGGER
type: MMLCommand
name: LST STGTRIGGER（查询融合计费消息缓存期间融合计费消息生成的trigger）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: STGTRIGGER
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- 融合计费消息缓存
status: active
---

# LST STGTRIGGER（查询融合计费消息缓存期间融合计费消息生成的trigger）

## 功能

**适用NF：SMF**

该命令用于显示融合计费消息缓存期间融合计费消息生成的trigger。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

无

## 操作的配置对象

- [[configobject/UNC/20.15.2/STGTRIGGER]] · 融合计费消息缓存期间融合计费消息生成的trigger（STGTRIGGER）

## 使用实例

显示融合计费消息缓存期间融合计费消息生成的trigger

```
%%LST STGTRIGGER:;%%
RETCODE = 0  操作成功

结果如下
--------
         时间阈值  =  立即上报
PDU时长阈值(分钟)  =  30
         流量阈值  =  立即上报
  PDU流量阈值(MB)  =  500
          RAT更新  =  立即上报
     服务节点更新  =  延迟上报
          QoS更新  =  延迟上报
     用户位置更新  =  延迟上报
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询融合计费消息缓存期间融合计费消息生成的trigger（LST-STGTRIGGER）_34667403.md`
