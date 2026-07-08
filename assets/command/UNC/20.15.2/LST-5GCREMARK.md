---
id: UNC@20.15.2@MMLCommand@LST 5GCREMARK
type: MMLCommand
name: LST 5GCREMARK（查询5GC QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: 5GCREMARK
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- 5GC QoS配置
- 5GC Qos映射ToS_DSCP
status: active
---

# LST 5GCREMARK（查询5GC QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SMF**

该命令用来查询5G用户配置的QoS参数到IP报头中DSCP（区别服务编码点）/TOS（服务类型）的映射规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：可选参数<br>参数含义：该参数指定QoS Profile的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数需要先通过ADD QOSPROFILE或者SET QOSGLOBAL命令配置。 |

## 操作的配置对象

- [[UNC@20.15.2@ConfigObject@5GCREMARK]] · 5GC QoS到TOS/DSCP的映射规则（5GCREMARK）

## 使用实例

- 查询给定QoS Profile名称对应的5GC Remark配置：
  ```
  %%LST 5GCREMARK: QOSPROFILENAME="profile";%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
    QoS Profile名  =  profile
              5QI  =  5
    ARP的优先级别  =  5
         标记类型  =  映射到Dscp
             DSCP  =  对应的DSCP的值为000000
           AF级别  =  0
     AF丢弃优先级  =  0
            TOS值  =  0
           DSCP值  =  0
  N3 DSCP配置开关  =  disable
          N3 DSCP  =  对应的DSCP的值为101110
        N3 AF级别  =  0
  N3 AF丢弃优先级  =  0
        N3 DSCP值  =  0
  N9 DSCP配置开关  =  disable
          N9 DSCP  =  对应的DSCP的值为101110
        N9 AF级别  =  0
  N9 AF丢弃优先级  =  0
        N9 DSCP值  =  0
  N6 DSCP配置开关  =  disable
          N6 DSCP  =  对应的DSCP的值为101110
        N6 AF级别  =  0
  N6 AF丢弃优先级  =  0
        N6 DSCP值  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询所有5GC Remark配置：
  ```
  %%LST 5GCREMARK:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
  QoS Profile名  5QI  ARP的优先级别  标记类型    DSCP                    AF级别  AF丢弃优先级  TOS值  DSCP值  N3 DSCP配置开关  N3 DSCP                 N3 AF级别  N3 AF丢弃优先级  N3 DSCP值  N9 DSCP配置开关  N9 DSCP                 N9 AF级别  N9 AF丢弃优先级  N9 DSCP值  N6 DSCP配置开关  N6 DSCP                 N6 AF级别  N6 AF丢弃优先级  N6 DSCP值  

  globalqos      6    6              映射到Dscp  对应的DSCP的值为101110  0       0             0      0       disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          
  profile        5    5              映射到Dscp  对应的DSCP的值为000000  0       0             0      0       disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          disable          对应的DSCP的值为101110  0          0                0          
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-5GCREMARK.md`
