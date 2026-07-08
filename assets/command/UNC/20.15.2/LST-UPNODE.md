---
id: UNC@20.15.2@MMLCommand@LST UPNODE
type: MMLCommand
name: LST UPNODE（查询UPF节点）
nf: UNC
version: 20.15.2
verb: LST
object_keyword: UPNODE
command_category: 查询类
applicable_nf:
- SMF
- SGW-C
- PGW-C
- GGSN
effect_mode: ''
is_dangerous: false
category_path:
- 业务服务管理
- 接口管理
- PFCP接口管理
- UP管理
- UP节点管理
status: active
---

# LST UPNODE（查询UPF节点）

## 功能

**适用NF：SMF、SGW-C、PGW-C、GGSN**

该命令用于查询指定实例名称的UPF节点特征。

## 注意事项

无

## 权限

G_1，管理员级别命令组；G_2，操作员级别命令组；G_3，用户级别命令组

## 参数

| 参数标识 | 参数名称 | 参数说明 |
| --- | --- | --- |
| NFINSTANCENAME | UPF实例名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。不区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF实例标识”参数取值保持一致时，关联关系生效。 |
| NFDESCNAME | UPF描述名称 | 可选必选说明：可选参数<br>参数含义：该参数用于指定UPF实例描述名称。<br>数据来源：全网规划<br>取值范围：字符串类型，输入长度范围是0~255。区分大小写。<br>默认值：无<br>配置原则：<br>本参数取值与ADD PNFPROFILE命令中的“NF描述名称”参数取值保持一致。 |

## 操作的配置对象

- [[configobject/UNC/20.15.2/UPNODE]] · UPF节点（UPNODE）

## 使用实例

- 查询实例名称为“upf_instance_1”的节点特征：
  ```
  %%LST UPNODE: NFINSTANCENAME="upf_instance_1";%%
  RETCODE = 0  操作成功

  结果如下
  --------
                                UPF实例名称  =  upf_instance_1
                                UPF位置特征  =  中心节点或本地节点
                                    UPF功能  =  无
                                      UPF锁  =  否
                  辅锚点UPF故障迁移功能开关  =  辅锚点UPF迁移功能关
                               地址分配属性  =  继承全局配置
                                UPF共享开关  =  不使能
                                    VPN名称  =  _public_
                      是否仅支持作为分流UPF  =  不使能
                      是否支持作为ATSSS UPF  =  不使能
                        IPv6 ND信息携带方式  =  私有信元方式
                               惯性运行开关  =  不使能
                                UPF描述名称  =  UPF-beijingRegion-beijing-toB-b001
                                园区UPF开关  =  不使能
                 ULCL UPF间创建转发隧道开关  =  不使能
  是否支持UPF无N9逻辑接口地址时作为锚点激活  =  不使能
                             是否支持5G LAN  =  不使能
                   主锚点与分流节点合设功能  =  不使能
                       是否支持组播广播业务  =  不使能
                               路径迁移开关  =  不使能
                       超时触发路径迁移开关  =  使能
              路径迁移响应等待时间(100毫秒)  =  10
               是否支持UE IP地址NAT转换功能  =  不使能
              UPF作为Proxy UPF对接PGW-U开关  =  不使能
                               质差分析开关  =  不使能
  是否支持作为智家随行场景To Home会话主锚点  =  不使能
                   信令触发静默路径迁移开关  =  不使能
                   路径迁移扩展信元携带开关  =  使能

  (结果个数 = 1)

  ---    END
  ```
- 查询所有UPF节点特征：
  ```
  %%LST UPNODE:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  UPF实例名称     UPF位置特征         UPF功能  UPF锁  辅锚点UPF故障迁移功能开关  地址分配属性  UPF共享开关  VPN名称   是否仅支持作为分流UPF  是否支持作为ATSSS UPF  IPv6 ND信息携带方式  惯性运行开关  UPF描述名称                         园区UPF开关  ULCL UPF间创建转发隧道开关  是否支持UPF无N9逻辑接口地址时作为锚点激活  是否支持5G LAN  主锚点与分流节点合设功能  是否支持组播广播业务  路径迁移开关  超时触发路径迁移开关  路径迁移响应等待时间(100毫秒)  是否支持UE IP地址NAT转换功能  UPF作为Proxy UPF对接PGW-U开关  质差分析开关   是否支持作为智家随行场景To Home会话主锚点  信令触发静默路径迁移开关  路径迁移扩展信元携带开关

  upf_instance_1  中心节点或本地节点  无       否     辅锚点UPF迁移功能关        继承全局配置  不使能       _public_  不使能                 不使能                 私有信元方式         不使能        UPF-beijingRegion-beijing-toB-b001  不使能       不使能                      不使能                                     不使能          不使能                    不使能                不使能        使能                  10                             不使能                        不使能                         不使能         不使能                                     不使能                    使能
  upf_instance_2  中心节点或本地节点  无       否     辅锚点UPF迁移功能关        继承全局配置  使能         _public_  不使能                 不使能                 私有信元方式         不使能        UPF-beijingRegion-beijing-toB-b002  不使能       不使能                      不使能                                     不使能          不使能                    不使能                不使能        使能                  10                             不使能                        不使能                         不使能         不使能                                     不使能                    使能
  (结果个数 = 2)

  ---    END
  ```

## 证据

- 原始手册：`evidence/UNC/20.15.2/查询UPF节点（LST-UPNODE）_09652974.md`
