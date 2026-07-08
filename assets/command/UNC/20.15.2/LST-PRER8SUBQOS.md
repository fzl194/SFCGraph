---
id: UNC@20.15.2@MMLCommand@LST PRER8SUBQOS
type: MMLCommand
name: LST PRER8SUBQOS（查询Pre-R8签约QoS配置）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: PRER8SUBQOS
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- PreR8 QoS配置
- 本地PreR8 QoS
status: active
---

# LST PRER8SUBQOS（查询Pre-R8签约QoS配置）

## 功能

**适用NF：GGSN**

该命令用于查询用户的签约QoS属性信息。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SUBQOSINDEX | 用户QoS索引 | 可选必选说明：可选参数<br>参数含义：该参数用于指定用户QoS索引值。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/PRER8SUBQOS]] · Pre-R8签约QoS配置（PRER8SUBQOS）

## 使用实例

查询SUBQOSINDEX为1的QoS签约信息：

```
%%LST PRER8SUBQOS: SUBQOSINDEX=1;%%
RETCODE = 0  操作成功

结果如下
--------
                  用户QoS索引  =  1
                        ARP值  =  高
会话类下行保证带宽(千比特/秒)  =  0
会话类上行保证带宽(千比特/秒)  =  0
会话类下行最大带宽(千比特/秒)  =  0
会话类上行最大带宽(千比特/秒)  =  0
  流类下行保证带宽(千比特/秒)  =  0
  流类上行保证带宽(千比特/秒)  =  0
  流类下行最大带宽(千比特/秒)  =  0
  流类上行最大带宽(千比特/秒)  =  7
交互类下行最大带宽(千比特/秒)  =  12
交互类上行最大带宽(千比特/秒)  =  0
                  交互类THP值  =  0
背景类下行最大带宽(千比特/秒)  =  0
背景类上行最大带宽(千比特/秒)  =  30222
                 最高业务级别  =  会话类
     超过最高业务级别时的处理  =  降级
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-PRER8SUBQOS.md`
