---
id: UNC@20.15.2@MMLCommand@ADD RDSUPFCTRL
type: MMLCommand
name: ADD RDSUPFCTRL（增加RADIUS服务器的UP列表中指定UP的功能属性）
nf: UNC
version: 20.15.2
verb: ADD
object_keyword: RDSUPFCTRL
command_category: 配置类
applicable_nf:
- SMF
- PGW-C
- GGSN
effect_mode: 立即生效
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- RADIUS管理
- RADIUS维护
- RADIUS UPF控制
status: active
---

# ADD RDSUPFCTRL（增加RADIUS服务器的UP列表中指定UP的功能属性）

## 功能

**适用NF：SMF、PGW-C、GGSN**

该命令用来增加RADIUS服务器使用的UP列表中指定UPF的功能属性。

## 注意事项

- 该命令执行后立即生效。

- 执行该命令时需保证UPLIST4RDS配置中已添加相同UPLISTNAME和UPINSTANCEID的配置。
- 如果新增记录优先级字段非0值时，则会在下一次二次鉴权RADIUS中转UPF会话创建时生效。

- 最多可输入512条记录。

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| UPLISTNAME | UP列表名称 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP列表名称。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~63。该参数需要是UPLIST4RDS配置中已添加的UPLISTNAME的值。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../../连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |
| UPINSTANCEID | UP实例标识 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP实例标识。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是1~36。该参数取值需要是UPLIST4RDS配置中已添加的UPINSTANCEID的值。不区分大小写。<br>默认值：无<br>配置原则：<br>该参数使用<br>[**ADD UPLIST4RDS**](../../连接管理/UP列表/向RADIUS服务器使用的UP列表中增加UP（ADD UPLIST4RDS）_52749060.md)<br>命令配置生成。 |
| PREFERENCE | 优先级 | 可选必选说明：必选参数<br>参数含义：该参数用于指定UP的优先级。<br>数据来源：本端规划<br>取值范围：整数类型，取值范围是0~255。<br>默认值：无<br>配置原则：<br>优先级值越大优先级越高，优先级值越小优先级越低。 |
| LOCKED | 锁定 | 可选必选说明：必选参数<br>参数含义：该参数用于对该UPF进行锁定操作，当取值为ENABLE时，SMF无法选择该UPF创建UPF中转RADIUS会话。<br>数据来源：本端规划<br>取值范围：<br>- DISABLE（不使能）<br>- ENABLE（使能）<br>默认值：无<br>配置原则：<br>该参数为ENABLE时，指定为锁定该UPF。该参数为DISABLE时，指定为解锁该UPF。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/RDSUPFCTRL]] · RADIUS服务器的UP列表中指定UP的功能属性（RDSUPFCTRL）

## 使用实例

增加UP列表名为“uplist1”，UP名为“up1”的主机，优先级的值为1，锁定为ENABLE：

```
ADD RDSUPFCTRL: UPLISTNAME="uplist1", UPINSTANCEID="up1",PREFERENCE=1,LOCKED=ENABLE;
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/增加RADIUS服务器的UP列表中指定UP的功能属性（ADD-RDSUPFCTRL）_35803148.md`
