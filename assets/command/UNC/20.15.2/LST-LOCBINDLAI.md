---
id: UNC@20.15.2@MMLCommand@LST LOCBINDLAI
type: MMLCommand
name: LST LOCBINDLAI（查询UPF位置信息与UPF优先支持的LAI范围的绑定关系）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: LOCBINDLAI
command_category: 查询类
applicable_nf:
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 会话管理
- 接入管理
- UPF选择管理
- 位置区域绑定LAI范围
status: active
---

# LST LOCBINDLAI（查询UPF位置信息与UPF优先支持的LAI范围的绑定关系）

## 功能

**适用NF：GGSN**

该命令用于查询UPF位置信息与UPF优先支持的LAI范围的绑定关系。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| LOCALITY | UPF位置区 | 可选必选说明：可选参数<br>参数含义：该参数用于标识UPF位置区。<br>数据来源：本端规划<br>取值范围：字符串类型，输入长度范围是1~255。<br>默认值：无<br>配置原则：<br>该参数需要与ADD PNFPROFILE命令中 “LOCALITY”的取值保持一致，参数匹配时大小写不敏感。 |
| LAI | LAI | 可选必选说明：可选参数<br>参数含义：该参数用于查询单个TAI绑定的LOCALITY。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是9~10。不区分大小写。<br>默认值：无<br>配置原则：<br>字符串类型，输入长度范围是9~10。后4位为16进制数，其余为10进制数。 |

## 操作的配置对象

- [UPF位置信息与UPF优先支持的LAI范围的绑定关系（LOCBINDLAI）](configobject/UNC/20.15.2/LOCBINDLAI.md)

## 使用实例

- 查询所有的UPF位置信息与UPF优先支持的LAI范围的绑定关系 LST LOCBINDLAI:;
  ```
  %%LST LOCBINDLAI:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  UPF位置区  移动国家码  移动网号  LAC起始号段  LAC终止号段  

  locality1  460         03        1301         1302         
  locality1  460         03        1303         1304         
  locality2  460         03        1305         1306         
  (结果个数 = 3)

  ---    END
  ```
- 查询特定的UPF位置信息与UPF优先支持的LAI范围的绑定关系，其中UPF位置区为“locality1” LST LOCBINDLAI: LAI="123031301";
  ```
  %%LST LOCBINDLAI: LAI="123031301";%%
  RETCODE = 0  操作成功

  结果如下
  --------
    UPF位置区  =  locality1
   移动国家码  =  460
     移动网号  =  03
  LAC起始号段  =  1301
  LAC终止号段  =  1302
  (结果个数 = 1)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF位置信息与UPF优先支持的LAI范围的绑定关系（LST-LOCBINDLAI）_96242187.md`
