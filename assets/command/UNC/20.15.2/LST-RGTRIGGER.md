---
id: UNC@20.15.2@MMLCommand@LST RGTRIGGER
type: MMLCommand
name: LST RGTRIGGER（查询RG级的trigger参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: RGTRIGGER
command_category: 查询类
applicable_nf:
- PGW-C
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 计费管理
- 融合计费
- RG级Trigger
status: active
---

# LST RGTRIGGER（查询RG级的trigger参数）

## 功能

**适用NF：PGW-C、SMF**

该命令用于查询RG级的trigger参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| CCTMPLTNAME | 融合计费模板名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定CCT模板的名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD CCT**](../融合计费模板/增加融合计费模板（ADD CCT）_09653176.md)<br>命令配置生成。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RGTRIGGER]] · RG级的trigger参数（RGTRIGGER）

## 使用实例

查询名为“test”的融合计费模板的RG级的trigger参数。

```
%%LST RGTRIGGER: CCTMPLTNAME="test";%%
RETCODE = 0  操作成功

结果如下
--------
    融合计费模板名称  =  test
             QoS更新  =  延迟上报
        用户位置更新  =  延迟上报
        服务节点更新  =  延迟上报
区域用户位置上报更新  =  延迟上报
  PS数据关闭状态更新  =  延迟上报
        用户时区更新  =  立即上报
            PLMN更新  =  立即上报
             RAT更新  =  立即上报
            时间阈值  =  延迟上报
            流量阈值  =  延迟上报
            事件阈值  =  延迟上报
            配额阈值  =  立即上报
        配额有效时长  =  立即上报
        配额保持时长  =  立即上报
服务PLMN速率控制更新  =  延迟上报
     APN速率控制更新  =  延迟上报
      跟踪区标识更新  =  不上报
             RAI更新  =  不上报
          CGISAI更新  =  不上报
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-RGTRIGGER.md`
