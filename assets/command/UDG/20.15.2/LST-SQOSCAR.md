---
id: UDG@20.15.2@MMLCommand@LST SQOSCAR
type: MMLCommand
name: LST SQOSCAR（查询流行为CAR配置）
nf: UDG
version: 20.15.2
verb: LST
object_keyword: SQOSCAR
command_category: 查询类
effect_mode: ''
is_dangerous: false
category_path:
- 平台服务管理
- VNRS功能管理
- IP服务
- 安全管理
- QoS管理
- 流行为CAR
status: active
---

# LST SQOSCAR（查询流行为CAR配置）

## 功能

该命令用来查询流行为CAR配置。

## 注意事项

该命令仅适用于非NP卡场景和NP卡非加速模式场景。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| BEHAVIORNAME | 流行为名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定流行为名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围为1～31。<br>默认值：无<br>配置原则：区分大小写，不支持空格。 |

## 操作的配置对象

- [[UDG@20.15.2@ConfigObject@SQOSCAR]] · 流行为CAR配置（SQOSCAR）

## 使用实例

查询流行为的CAR配置：

```
LST SQOSCAR:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
           流行为名称  =  b1
 承诺信息速率（kbps）  =  10
     峰值速率（kbps）  =  100
承诺突发尺寸（bytes）  =  20
超出突发尺寸（bytes）  =  200
       绿色报文的动作  =  报文重标记服务等级和颜色
   绿色报文的服务等级  =  确保转发等级1
 绿色报文的重标记颜色  =  绿
       黄色报文的动作  =  报文通过
   黄色报文的服务等级  =  无效的服务等级
 黄色报文的重标记颜色  =  无效的颜色类型
       红色报文的动作  =  报文丢弃
   红色报文的服务等级  =  无效的服务等级
 红色报文的重标记颜色  =  无效的颜色类型
             色敏模式  =  色敏
(结果个数 = 1)
---    END
```

## 证据

- 原始手册：`evidence/UDG/20.15.2/LST-SQOSCAR.md`
