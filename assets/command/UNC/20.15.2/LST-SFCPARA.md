---
id: UNC@20.15.2@MMLCommand@LST SFCPARA
type: MMLCommand
name: LST SFCPARA（查询SFC参数）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: SFCPARA
command_category: 查询类
applicable_nf:
- AMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 5G接入业务管理
- 感知业务管理
- 感知控制面功能参数
status: active
---

# LST SFCPARA（查询SFC参数）

## 功能

**适用NF：AMF**

在部署感知的场景下，通过LST SFCPARA查询SFC的参数。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| SFCINSTANCEID | SFC实例ID | 可选必选说明：可选参数<br>参数含义：该参数用于指定SFC网元的实例ID。<br>数据来源：对端协商<br>取值范围：字符串类型，输入长度范围是1~64。只允许输入十进制数字（0-9），除0之外不能以0开头。对应十进制数取值范围是0~4294967295。<br>默认值：无<br>配置原则：无 |

## 操作的配置对象

- [SFC参数（SFCPARA）](configobject/UNC/20.15.2/SFCPARA.md)

## 使用实例

若运营商想查询SFC实例ID为1的SFC参数信息，可以用如下命令：

```
%%LST SFCPARA: SFCINSTANCEID="1";%%
RETCODE = 0  操作成功

结果如下
------------------------
SFC实例ID  =  1
    IP类型  =  IPv4
  IPv4地址  =  192.168.4.15
  IPv6地址  =  ::
    端口号  =  80
(结果个数 = 1)

---    END
```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询SFC参数（LST-SFCPARA）_83159234.md`
