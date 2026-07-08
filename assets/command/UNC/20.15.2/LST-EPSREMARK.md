---
id: UNC@20.15.2@MMLCommand@LST EPSREMARK
type: MMLCommand
name: LST EPSREMARK（查询EPS QoS到TOS/DSCP的映射规则）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: EPSREMARK
command_category: 查询类
applicable_nf:
- SGW-C
- PGW-C
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- QoS
- EPS QoS配置
- EPS Qos映射ToS_DSCP
status: active
---

# LST EPSREMARK（查询EPS QoS到TOS/DSCP的映射规则）

## 功能

**适用NF：SGW-C、PGW-C**

该命令用来显示UNC上在SAE架构下配置的QoS参数到IP报头中DSCP（区别服务编码点）/TOS（服务类型）的映射规则。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| QOSPROFILENAME | QoS Profile名称 | 可选必选说明：可选参数<br>参数含义：该参数指定QoS Profile的名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~63。不区分大小写。<br>默认值：无<br>配置原则：<br>QOSPROFILENAME字段值必须先在QOSPROFILE或QOSGLOBAL对象中添加成功，可以通过LST QOSPROFILE或LST QOSGLOBAL命令查询。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/EPSREMARK]] · EPS QoS到TOS/DSCP的映射规则（EPSREMARK）

## 使用实例

指定QoS Profile名，显示EpsRemark配置信息：

```
%%LST EPSREMARK: QOSPROFILENAME="globalqos";%%
RETCODE = 0  操作成功

结果如下
--------
       QoS Profile名  =  globalqos
              AF级别  =  0
        AF丢弃优先级  =  0
                DSCP  =  对应的DSCP的值为101110
            标记类型  =  映射到Dscp
               TOS值  =  0
       ARP的优先级别  =  15
                 QCI  =  1
              DSCP值  =  0
   S1-U DSCP配置开关  =  使能
           S1-U DSCP  =  映射的DSCP值
         S1-U AF级别  =  0
   S1-U AF丢弃优先级  =  0
         S1-U DSCP值  =  22
 SGW S5 DSCP配置开关  =  使能
         SGW S5 DSCP  =  映射的DSCP值
       SGW S5 AF级别  =  0
 SGW S5 AF丢弃优先级  =  0
       SGW S5 DSCP值  =  23
 PGW S5 DSCP配置开关  =  使能
         PGW S5 DSCP  =  映射的DSCP值
       PGW S5 AF级别  =  0
 PGW S5 AF丢弃优先级  =  0
       PGW S5 DSCP值  =  24
 SGW S8 DSCP配置开关  =  使能
         SGW S8 DSCP  =  映射的DSCP值
       SGW S8 AF级别  =  0
 SGW S8 AF丢弃优先级  =  0
       SGW S8 DSCP值  =  25
 PGW S8 DSCP配置开关  =  使能
         PGW S8 DSCP  =  映射的DSCP值
       PGW S8 AF级别  =  0
 PGW S8 AF丢弃优先级  =  0
       PGW S8 DSCP值  =  26
PGW SGi DSCP配置开关  =  使能
        PGW SGi DSCP  =  映射的DSCP值
      PGW SGi AF级别  =  0
PGW SGi AF丢弃优先级  =  0
      PGW SGi DSCP值  =  27
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-EPSREMARK.md`
