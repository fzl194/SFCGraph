---
id: UNC@20.15.2@MMLCommand@LST LOCBINDN2TAI
type: MMLCommand
name: LST LOCBINDN2TAI（查询UPF位置信息与UPF优先支持的5G TAI范围的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCBINDN2TAI
command_category: 查询类
applicable_nf:
- SMF
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 位置区域绑定5G TAI范围
status: active
---

# LST LOCBINDN2TAI（查询UPF位置信息与UPF优先支持的5G TAI范围的绑定关系）

## 功能

**适用NF：SMF**

该命令用于查询UPF位置信息与UPF优先支持的TAI范围的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALITY | UPF位置区 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF位置区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>该参数需要与ADD PNFPROFILE命令中 “LOCALITY”的取值保持一致，参数匹配时大小写不敏感。 |
| TAI | TAI | 可选必选说明：可选参数<br>参数含义：该参数用于查询单个TAI绑定的LOCALITY。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是11~12。不区分大小写。<br>默认值：无<br>配置原则：<br>字符串类型，输入长度范围是11~12。后6位为16进制数，其余为10进制数。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/LOCBINDN2TAI]] · UPF位置信息与UPF优先支持的5G TAI范围的绑定关系（LOCBINDN2TAI）

## 使用实例

- 查询所有的UPF位置信息与UPF优先支持的TAI范围的绑定关系 LST LOCBINDN2TAI:;
  ```
  %%LST LOCBINDN2TAI:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  UPF位置区  移动国家码  移动网号  N2 TAC起始号段  N2 TAC终止号段  

  locality1  460         03        130101          130102          
  locality1  460         03        130103          130104          
  locality2  460         03        130105          130106          
  (结果个数 = 3)

  ---    END
  ```
- 查询特定的UPF位置信息与UPF优先支持的TAI范围的绑定关系，其中UPF位置区为“locality1” LST LOCBINDN2TAI: TAI="12303130101";
  ```
  %%LST LOCBINDN2TAI: TAI="12303130101";%%
  RETCODE = 0  操作成功

  结果如下
  --------
       UPF位置区  =  locality1
      移动国家码  =  460
        移动网号  =  03
  N2 TAC起始号段  =  130101
  N2 TAC终止号段  =  130102
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/LST-LOCBINDN2TAI.md`
